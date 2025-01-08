#DATE CREATED:JAN 8,2025
#QUANG
#FIRST PYTHON PROGRAM


from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import os
from datetime import date
path='Database(QUANG).txt'

def add():
    line = id.get() + '-'+ name.get() + '-' + year.get()
    save(line)
    show()

def show():
    name=read() 
    listbox.delete(0,END)
    for i in name:
        listbox.insert(END,i)


def save(line):
    try:
        f = open(path,'a',encoding='utf8')
        f.writelines(line)
        f.writelines('\n')
        f.close()
    except:
        with open("Database(QUANG).txt", "w") as file:
            file.close()
def read():
    name = []
    try:
        f = open(path,'r',encoding='utf8')
        for i in f:
            data = i.strip()
            arr = data.split('-')
            name.append(arr)
        f.close()
    except:
        with open("Database(QUANG).txt", "w") as file:
            file.close()
    return name

def deleteall():
    res=mb.askquestion('Delete All Data', 'Do you really want to delete all data ?\n(THIS ACTION CANNOT BE UNDONE)',icon='warning')
    if res == 'yes' :
        f = open(path,'w',encoding='utf8')
        f.close()
        listbox.delete(0,END)
        mb.showinfo('ALert', 'All data deleted.')
    else :
        mb.showinfo('User canceled', 'Nothing happened to your data.')


def exit():
    res=mb.askquestion('Alert', 'Are you sure want to exit ?', icon='warning')
    if res == 'yes' :
        root.destroy()

def sort():
    name = read()
    for i in range(len(name)):
        for j in range(len(name)):
            x,y = name[i],name[j]
            if x[2] > y[2]:
                name[i],name[j] = y,x
    listbox.delete(0,END)
    for i in name:
        listbox.insert(END,i)

def view():
    os.startfile('Database(QUANG).txt')


def delete():
    file = open('Database(QUANG).txt', 'rb')
    pos = next = 0
    for line in file:
        pos = next
        next += len(line)
    file = open('Database(QUANG).txt', 'ab')
    with open('Database(QUANG).txt', 'r') as files:
        lines = len(files.readlines())
    file.truncate(pos)
    listbox.delete(lines)
    show()

def select():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        file = open('Database(QUANG).txt', 'rb')
        pos = next = 0
        for line in file:
            pos = next
            next += len(line)
        file = open('Database(QUANG).txt', 'ab')
        file.truncate(pos)

def msg():
        res=mb.askquestion('Alert', 'Are you sure want to exit ?', icon='warning')
        if res == 'yes' :
            root.destroy()

today = date.today()
d2 = today.strftime("%B %d, %Y")


root = Tk()

id=StringVar()
name = StringVar()
year = StringVar()
root.title('PEOPLE MANAGEMENT PROGRAM (QUANG)')
root.configure(background='#b8c7ff')
root.minsize(height=480,width=600)
Label(root, text ='PEOPLE MANAGER',fg='white',font=('cambria',16),width=20,background='#1138d4').grid(row=0)
listbox = Listbox(root,width=100,height=20,bg='#37498c',fg='white')
listbox.grid(row=1,columnspan=2)
show()
Label(root, text ='ID Number:',fg='#102887',font=('cambria',13),width=20,background='#b8c7ff').grid(row=2)
Entry(root,width=40,textvariable=id,background='#9daff2',selectbackground='#37498c',selectforeground='white').grid(row=2,column=1)
Label(root, text ='Name:',fg='#102887',font=('cambria',13),width=20,background='#b8c7ff').grid(row=3)
Entry(root,width=40,textvariable=name,background='#9daff2',selectbackground='#37498c',selectforeground='white').grid(row=3,column=1)
Label(root, text ='Year of birth:',fg='#102887',font=('cambria',13),width=20,background='#b8c7ff').grid(row=4)
Entry(root,width=40,textvariable=year,background='#9daff2',selectbackground='#37498c',selectforeground='white').grid(row=4,column=1)
button = Frame(root)
Button(button,text= 'Add',command = add,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
Button(button,text= 'View File', command= view,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
Button(button,text= 'Arrange', command=sort,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
Button(button,text= 'Delete Last Line',command=delete,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
Button(button,text= 'Delete All',command=deleteall,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
Button(button,text= 'Exit',command=exit,background='#1138d4',foreground='white',activebackground='#365df7',activeforeground='white').pack(side=LEFT)
button.grid(row=5,column=1)

Label(root, text =d2,fg='white',font=('cambria',13),width=20,background='#1138d4').grid(row=0,column=1)
root.protocol('WM_DELETE_WINDOW', msg)
root.mainloop()