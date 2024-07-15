from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox 
import sqlite3

window = Tk()
window.title('Hope Hospital')
window.iconbitmap("icon.ico")

window.minsize(height=900,width=700)
window.maxsize(height=900,width=700)
#window.resizable(0,0)

conn = sqlite3.connect('Patients_ho.db')
c = conn.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS patients(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         first_name TEXT,
         last_name TEXT,
         Age INT,
         Blood TEXT,
         Contact INT,
         Email TEXT,
         Address TEXT,
         Password TEXT,
         Gender TEXT
        )'''
)
conn.commit()
conn.close()

window.minsize(height=900,width=700)
window.maxsize(height=900,width=700)

def submitted():
     c =PASSWORD.get()
     d = Con_pass.get()
     if c != d:
        messagebox.showinfo("showinfo", "The password doesnot match") 
     else :
        conn = sqlite3.connect('Patients_ho.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO patients (first_name,last_name,Age,Blood,Contact,Email,Address,Password) VALUES(?,?,?,?,?,?,?,?)",
            (First_name.get(),Last_name.get(),e3.get(),e4.get(),e5.get(),e6.get(),address.get(),PASSWORD.get()),
        )
        conn.commit()
        conn.close()
        First_name.delete(0,END)
        Last_name.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        address.delete(0,END)

        window.destroy()
        window2=Tk()
        window2.title("Hope Hospital")
        window2.minsize(height=300,width=400)
        window2.maxsize(height=300,width=400)
        lbl1=Label(window2, text="You have succesfully registered.", font=15)
        lbl1.place(x=50,y=120)
        btn1=Button(window2, text="Go To HomePage",font=("Calibri",10))
        btn1.place(x=150,y=180)



l=Label(window,text="Fill all the details.",font =("Arial Bold",20))
l.pack()
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
First_name= Entry(window,width=25,font=("Calibri",10))
First_name.place(x=180,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
Last_name = Entry(window,width=25,font=("Calibri",10))
Last_name.place(x =180,y=105)
l3= Label(window,text="Age",font=50)
l3.place(x=0,y=150)

e3= Entry(window,width=25,font=("Calibri",10))
e3.place(x=180,y=150)
adress=Label(window,text="Address",font=50)
adress.place(x=0,y=200)
address= Entry(window,width=25,font=("Calibri",10))
address.place(x=180,y=200)
l4= Label(window,text="Blood Group",font=50)
l4.place(x=0,y=250)
e4= Entry(window,width=25,font=("Calibri",10))
e4.place(x=180,y=255)
l5= Label(window,text="Contact",font=50)
l5.place(x=0,y=300)
e5= Entry(window,width=25,font=("Calibri",10))
e5.place(x=180,y=305)
l6= Label(window,text="Email",font=50)
l6.place(x=0,y=350)
e6= Entry(window,width=25,font=("Calibri",10))
e6.place(x=180,y=355)
b1=Button(text='Submit',font=("Calibri",12),command=submitted)
b1.place(x=205,y=670)

l8= Label(window,text="Password",font=50)
l8.place(x=0,y=400)
PASSWORD =Entry(window,width=25,font=("Calibri",10)) 
PASSWORD.place(x=180,y=402)
l9 = Label(window,text="Confrim Password",font=20)
l9.place(x=0,y=460)
Con_pass= Entry(window,width=25,font=("Calibri",10))
Con_pass.place(x=180,y=460)


def gender1():
    text=var.get()
    gender = 'Male' if text == 1 else 'Female'

g=Label(text="Gender:",font=("Arial Bold",15))
g.place(x=0,y=545)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,font=20,value=1,command=gender1)
r1.place(x=0,y=585)
r2=Radiobutton(window,text="Female",variable=var,value=2,font=20,command=gender1)
r2.place(x=0,y=610)
r3=Radiobutton(window,text="Others",variable=var,value=3,font=20,command=gender1)
r3.place(x=0,y=635)

photo2=Image.open("o4.png")
resize_photo2=photo2.resize((400,500))
final_image2=ImageTk.PhotoImage(resize_photo2)
picture=Label(window, image=final_image2, width=0, height=600)
picture.place(x=390,y=40)


mainloop()