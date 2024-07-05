from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox 
import sqlite3

window = Tk()
window.title('Patient Registration')

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
          Password TEXT
         )'''
)
conn.commit()
conn.close()

window.minsize(height=900,width=900)
window.maxsize(height=900,width=900)

def submitted():
     c =PASSWORD.get()
     d = Con_pass.get()
     if c != d:
        messagebox.showinfo("showinfo", "The password doesnot match") 
     else :
        conn = sqlite3.connect('Patients_ho.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO employee(first_name,last_name,Age,Blood,Contact,Email,Address,Password) VALUES(?,?,?,?,?,?,?)",
            (First_name.get(),Last_name.get(),AGE.get(),Blood_grp.get(),Cont.get(),Email.get(),Addr.get(),PASSWORD.get()),
        )
        conn.commit()
        conn.close()
        First_name.delete(0,END)
        Last_name.delte(0,END)
        AGE.delete(0,END)
        Blood_grp.delete(0,END)
        Cont.delete(0,END)
        Email.delete(0,END)
        Addr.delete(0,END)

        window.destroy()
        window2=Tk()
        window2.title("Hope Hospital")
        window2.minsize(height=300,width=400)
        window2.maxsize(height=300,width=400)
        lbl1=Label(window2, text="You have succesfully registered.", font=15)
        lbl1.place(x=50,y=120)
        btn1=Button(window2, text="Go To HomePage",font=("Calibri",10))
        btn1.place(x=150,y=180)



l=Label(window,text="Fill all the details.",font = 100)
l.pack()
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
First_name= Entry(window,width=20,font=("Calibri",10))
First_name.place(x=120,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
Last_name = Entry(window,width=20,font=("Calibri",10))
Last_name.place(x =120,y=105)
l3= Label(window,text="Age",font=50)
l3.place(x=0,y=150)
AGE= Entry(window,width=20,font=("Calibri",10))
AGE.place(x=120,y=150)
l4= Label(window,text="Blood Group",font=50)
l4.place(x=0,y=200)
Blood_grp= Entry(window,width=20,font=("Calibri",10))
Blood_grp.place(x=120,y=205)
l5= Label(window,text="Contact",font=50)
l5.place(x=0,y=250)
Cont= Entry(window,width=20,font=("Calibri",10))
Cont.place(x=120,y=255)
l6= Label(window,text="Email",font=50)
l6.place(x=0,y=300)
Email= Entry(window,width=25,font=("Calibri",10))
Email.place(x=120,y=305)
l7 = Label(window,text="Address",font=50)
l7.place(x=0,y=350)
Addr= Entry(window,width=20,font=("Calibri",10))
Addr.place(x=120,y=352)
l8= Label(window,text="Password",font=50)
l8.place(x=0,y=400)
PASSWORD =Entry(window,width=20,font=("Calibri",10)) 
PASSWORD.place(x=120,y=402)
l9 = Label(window,text="Confrim Password",font=20)
l9.place(x=0,y=460)
Con_pass= Entry(window,width=20,font=("Calibri",10))
Con_pass.place(x=140,y=462)
b1=Button(text='Submit',font=("Calibri",20),command=submitted)
b1.place(x=250,y=600)


def gender():
    text=var.get()


g=Label(text="Gender:",font=("Arial Bold",15))
g.place(x=0,y=545)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,font=20,value=1,command=gender)
r1.place(x=0,y=585)
r2=Radiobutton(window,text="Female",variable=var,value=2,font=20,command=gender)
r2.place(x=0,y=610)
r3=Radiobutton(window,text="Others",variable=var,value=3,font=20,command=gender)
r3.place(x=0,y=635)

photo2=Image.open("o4.png")
resize_photo2=photo2.resize((600,600))
final_image2=ImageTk.PhotoImage(resize_photo2)
picture=Label(window, image=final_image2, width=0, height=600)
picture.place(x=390,y=20)


mainloop()