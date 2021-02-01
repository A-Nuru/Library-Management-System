#################        IMPORTING THE LIBRARIES          ################



import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import time
import datetime
from datetime import date
import random
from twilio.rest import Client










##################          STUDENT LOGIN DATABASE           ##############

def student_Database():
    global conn0, cursor0
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    conn0.commit()

    login_stu()

    



##################          ADMIN LOGIN DATABASE              ##############

def admin_Database():
    global conn, cursor
    conn = sqlite3.connect("Admin.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor.execute('DELETE FROM login')
    cursor.execute("INSERT INTO login (username, password,mobile_no) VALUES('uellibrary', 'uel123',+447388397814)")
    conn.commit()
    
    login()





##################       STUDENT LOGIN AUTHORIZATION        ##############

def login_stu():
    global name, password
    name = name_entry.get()
    password = password_entry.get()

    conn0 = sqlite3.connect('Student.db')
    cursor0 = conn0.cursor()
    cursor0.execute('select username, password from login')
    k = []
    for row in cursor0:
        if row[0] == name and row[1] == password:
            k.append(row[0])
            k.append(row[1])

    if len(k) == 2:
        Frame9()
        k.clear()
    else:
        messagebox.showinfo('Error','Username or Password Incorrect')

        
    

##################        ADMIN LOGIN AUTHORIZATION         ##############

def login():
    name = name_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('Admin.db')
    cursor = conn.cursor()
    cursor.execute('select username, password from login')
    k = []
    for row in cursor:
        if row[0] == name and row[1] == password:
            k.append(row[0])
            k.append(row[1])

    if len(k) == 2:
        Frame3()
        k.clear()
    else:
        messagebox.showinfo('Error','Username or Password Incorrect')




##################                          FRAME-5  (ADMIN REGISTERING NEW MEMBERS)                       ##############
    
def Frame5():
    show_frame(frame5)
    global stu_uname, stu_pw, stu_ph

    Label(frame5,text = 'Username : ',font = ('times',15,'bold italic')).place(x=100,y=150)
    stu_uname=StringVar()
    Entry(frame5, textvariable = stu_uname).place(x=280,y=150)

    Label(frame5,text = 'Password : ',font = ('times',15,'bold italic')).place(x=100,y=200)
    stu_pw=StringVar()
    Entry(frame5, textvariable = stu_pw).place(x=280,y=200)

    Label(frame5,text = 'Phone number : ',font = ('times',15,'bold italic')).place(x=100,y=250)
    stu_ph=StringVar()
    Entry(frame5, textvariable = stu_ph).place(x=280,y=250)

    Button(frame5, text = 'Submit',font = ('times',15,'bold italic')).place(x=300,y=300)

    Button(frame5, text = 'Back', command = Frame3,font = ('times',15,'bold italic')).place(x=220,y=300)




##################                          FRAME-3  (ADMIN OPERATIONS)                       ##############

    
def Frame3():
    show_frame(frame3)
    
    Button(frame3, text = 'Add Book', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=100)
    Button(frame3, text = 'Add Members', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=170)
    Button(frame3, text = 'Issue Book', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=240)
    Button(frame3, text = 'Check Record', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=310)
    Button(frame3, text = 'Reminder', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=370)


    Button(frame3, text = 'Logout', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=450)

    




  

##################                          FRAME-2A  (STUDENT LOGIN PAGE)                      ##############


def Frame2a():
    show_frame(frame2a)

    global name_entry
    global password_entry

    Label(frame2a, text = 'Username : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=170)
    Label(frame2a, text = 'Password : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=240)

    name_entry=StringVar()
    Entry(frame2a,textvariable=name_entry).place(x=170,y=170)

    password_entry=StringVar()
    Entry(frame2a,textvariable=password_entry, show = '*').place(x=170,y=240)
    
    Button(frame2a, text = 'Sign In',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=320)
    Button(frame2a, text = 'Go Back',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=380)






##################                          FRAME-2  (ADMIN LOGIN PAGE)                       ##############


def Frame2():
    show_frame(frame2)
    global name_entry
    global password_entry

    Label(frame2, text = 'Username : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=170)
    Label(frame2, text = 'Password : ',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=50,y=240)

    name_entry=StringVar()
    Entry(frame2,textvariable=name_entry).place(x=170,y=170)

    password_entry=StringVar()
    Entry(frame2,textvariable=password_entry, show = '*').place(x=170,y=240)
    
    Button(frame2, text = 'Sign In',command = admin_Database ,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=320)
    Button(frame2, text = 'Go Back',command = Frame1,font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=380)




##################                          FRAME-1  (HOME PAGE)                       ##############


def Frame1():
    show_frame(frame1)
    Label(frame1, text = 'Login as Admin : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=170)
    Button(frame1, text = 'Sign In',command = Frame2, bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=170)

    Label(frame1, text = 'Login as Student : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=270)
    Button(frame1, text = 'Sign In',command = Frame2a, bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=270)

    Label(frame1,text = 'Have  to Register?',font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=370)
    Button(frame1, text = 'Sign Up',font = ('times',15,'bold italic'),bg='#E0FFFF').place(x=800,y=370)

    Button(frame1, text = 'Exit',command = close, bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=700,y=450)



##################              FUNCTION TO EXIT THE APPLICATION             ##############


def close():
    root.destroy()



##################              FUNCTION TO RAISE DESIRED FRAMES             ##############

     
def show_frame(frame):
    frame.tkraise()

    


##################                       MAIN WINDOW                         ##############


root = tk.Tk()
root.title('UEL Library')
root.geometry('1000x650')
root.resizable(0,0)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)





##################          RENDERING     FRAMES  ON MAIN WINDOW         ##############


frame1 = Frame(root)
frame2 = Frame(root)
frame2a = Frame(root)
frame3 = Frame(root)

for frame in (frame1,frame2,frame2a, frame3):
    frame.place(relheight=1,relwidth=1)



Frame1()                   # Running first frame
 


root.mainloop()

