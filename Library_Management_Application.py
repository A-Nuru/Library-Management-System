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







##################        ADDING THE REGISTRATION DETAILS INTO DATABSE FOR USERS REGISTERING BY THEMSELVES        #######################


def stu_self_in():
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    
    if (unames and pws and phs)=='':
        messagebox.showinfo('Error', 'Fields cannot be empty')
    else:
        cursor0.execute("INSERT INTO login (username, password,mobile_no) VALUES(?,?,?)",(unames,pws,phs))
        conn0.commit()
        messagebox.showinfo("Success","Registered Successfully")
        show_frame(frame1)



##################        CHECKING IF THE USERNAME ALREADY EXISTS BEFORE REGISTRATION          ##############


def Stu_self_register():
    global unames,pws,phs
    
    unames = stu_unames.get()
    pws = stu_pws.get()
    phs = stu_phs.get()

    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor0.execute('select username from login')

    s=[]
    
    for row in cursor0:
        if row[0] == unames:
            s.append(row[0])
    
    if len(s)>=1:
        messagebox.showinfo('Error', 'Username Already Exists, Choose Another One!')
        s.clear()
    else:
        stu_self_in()


################          ADDING THE REGISTRATION DETAILS INTO DATABSE         ################


    
def stu_in():
    
    conn0 = sqlite3.connect("Student.db")
    cursor0 = conn0.cursor()
    
    if (uname and pw and ph)=='':
        messagebox.showinfo('Error', 'Fields cannot be empty')                           #      THIS BLOCK IS ACCESSED WHEN ADMIN WANTS TO ADD NEW MEMBERS
    else:
        cursor0.execute("INSERT INTO login (username, password,mobile_no) VALUES(?,?,?)",(uname,pw,ph))
        conn0.commit()
        messagebox.showinfo("Success","Registered Successfully")
        show_frame(frame3)




##################        CHECKING IF THE USERNAME ALREADY EXISTS BEFORE REGISTRATION          ##############



def Stu_register():
    global uname,pw,ph
    
    uname = stu_uname.get()
    pw = stu_pw.get()
    ph = stu_ph.get()

    conn0 = sqlite3.connect("Student.db")                                          #        THIS BLOCK IS ACCESSED WHEN ADMIN WANTS TO ADD NEW MEMBERS
    cursor0 = conn0.cursor()
    cursor0.execute("CREATE TABLE IF NOT EXISTS login (username TEXT , password TEXT, mobile_no TEXT)")
    cursor0.execute('select username from login')

    s=[]
    
    for row in cursor0:
        if row[0] == uname:
            s.append(row[0])
            
    if len(s)>=1:
        messagebox.showinfo('Error', 'Username Already Exists, Choose Another One!')
        s.clear()
    else:
        stu_in()




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
    cursor.execute("INSERT INTO login (username, password, mobile_no) VALUES('uellibrary', 'uel123',+447727161208)")
    conn.commit()
    
    login()


##################        BOOKS DETAILS DATABASE         ##############

        
def books_database():
    global conn1, cursor1
    conn1 = sqlite3.connect('books.db')
    cursor1 = conn1.cursor()
    cursor1.execute((''' create table if not exists book
        (Name text not null,
        Author text not null,
        Genre text not null,
        Copies text not null,
        Location text not null)'''))
    print('Table Created')
    




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






##################                          FRAME-5A (USERS SELF-REGISTRATION)                    ##############



def Frame5a():
    show_frame(frame5a)
    
    global stu_unames, stu_pws, stu_phs

    Label(frame5a,text = 'Username : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=150)
    stu_unames=StringVar()
    Entry(frame5a, textvariable = stu_unames).place(x=280,y=150)

    Label(frame5a,text = 'Password : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=200)
    stu_pws = StringVar()
    Entry(frame5a, textvariable = stu_pws).place(x=280,y=200)

    Label(frame5a,text = 'Phone number : ',font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=100,y=250)
    stu_phs = StringVar()
    Entry(frame5a, textvariable = stu_phs).place(x=280,y=250)

    Button(frame5a, text = 'Submit', command=Stu_self_register,font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=300,y=300)

    Button(frame5a, text = 'Back', command = Frame1, font = ('times',15,'bold italic'),bg = '#FFFFFF').place(x=220,y=300)





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

    Button(frame5, text = 'Submit', command = Stu_register,font = ('times',15,'bold italic')).place(x=300,y=300)

    Button(frame5, text = 'Back', command = Frame3,font = ('times',15,'bold italic')).place(x=220,y=300)




    ##################                          FRAME-4  (ADDING BOOK PAGE)                       ##############


def Frame4():
    show_frame(frame4)
    global book_name,book_author,book_genre,book_copies,book_location
    
    Label(frame4, text = 'Book Name : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=150)
    book_name=StringVar()
    Entry(frame4, textvariable = book_name).place(x=280,y=150)

    Label(frame4, text = 'Author : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=200)
    book_author=StringVar()
    Entry(frame4, textvariable = book_author).place(x=280,y=200)

    Label(frame4, text = 'Genre : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=250)
    book_genre=StringVar()
    Entry(frame4, textvariable = book_genre).place(x=280,y=250)

    Label(frame4, text = 'Copies : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=300)
    book_copies=StringVar()
    Entry(frame4, textvariable = book_copies).place(x=280,y=300)

    Label(frame4, text = 'Location : ',font = ('times',15,'bold italic'),bg = '#FFFFE0').place(x=100,y=350)
    book_location=StringVar()
    Entry(frame4, textvariable = book_location).place(x=280,y=350)


    




##################                          FRAME-3  (ADMIN OPERATIONS)                       ##############

    
def Frame3():
    show_frame(frame3)
    
    Button(frame3, text = 'Add Book', command = books_database, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=100)
    Button(frame3, text = 'Add Members', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=170)
    Button(frame3, text = 'Issue Book', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=240)
    Button(frame3, text = 'Check Record', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=310)
    Button(frame3, text = 'Reminder', font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=370)


    Button(frame3, text = 'Logout', command = Frame1, font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=500,y=450)

    




  

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

