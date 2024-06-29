from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title('Patient Registration')

window.minsize(height=500,width=600)

l=Label(window,text="Fill all the details,mandatory fields are marked with '*'",font = 100)
l.place(x=0)
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
e1= Entry(window,width=20,font=("Calibri",10))
e1.place(x=100,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
e2 = Entry(window,width=20,font=("Calibri",10))
e2.place(x =100,y=105)
l3= Label(window,text="Age",font=50)
l3.place(x=0,y=285)
e3= Entry(window,width=20,font=("Calibri",10))
e3.place(x=40,y=290)
l4= Label(window,text="Blood Group",font=50)
l4.place(x=0,y=325)
e4= Entry(window,width=20,font=("Calibri",10))
e4.place(x=120,y=330)
l5= Label(window,text="Contact",font=50)
l5.place(x=0,y=365)
e5= Entry(window,width=20,font=("Calibri",10))
e5.place(x=80,y=370)
b1=Button(text='Submit',font=("Calibri",12))
b1.place(x=205,y=410)


def gender():
    text=var.get()


g=Label(text="Gender:",font=("Arial Bold",15))
g.place(x=0,y=150)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,font=20,value=1,command=gender)
r1.place(x=0,y=180)
r2=Radiobutton(window,text="Female",variable=var,value=2,font=20,command=gender)
r2.place(x=0,y=210)
r3=Radiobutton(window,text="Others",variable=var,value=3,font=20,command=gender)
r3.place(x=0,y=240)

mainloop()


