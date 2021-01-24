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
    
    Button(frame2, text = 'Sign In',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=320)
    Button(frame2, text = 'Go Back',font = ('times',15,'bold italic'),bg='#FFFFFF').place(x=120,y=380)




##################                          FRAME-1  (HOME PAGE)                       ##############


def Frame1():
    show_frame(frame1)
    Label(frame1, text = 'Login as Admin : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=170)
    Button(frame1, text = 'Sign In', bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=170)

    Label(frame1, text = 'Login as Student : ', font = ('times',20,'bold italic'),bg='#E0FFFF').place(x=530,y=270)
    Button(frame1, text = 'Sign In',bg='#E0FFFF',font = ('times',15,'bold italic')).place(x=800,y=270)

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

frame1.place(relheight=1,relwidth=1)


Frame1()                   # Running first frame
 


root.mainloop()

