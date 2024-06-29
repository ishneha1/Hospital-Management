from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title('Patient Registration')
l=Label(window,text="Fill all the details,mandatory fields are marked with '*'",font = 100)
l.place(x= 250)
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
e1= Entry(window,width=20,font=("Calibri",10))
e1.place(x=100,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
e2 = Entry(window,width=20,font=("Calibri",10))
e2.place(x =100,y=105)

def gender():
    text=var.get()


g=Label(text="Gender:",font=("Arial Bold",20))
g.place(x=0,y=150)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,font=20,value=1,command=gender)
r1.place(x=0,y=180)
r2=Radiobutton(window,text="Female",variable=var,value=2,font=20,command=gender)
r2.place(x=0,y=210)
r3=Radiobutton(window,text="Others",variable=var,value=3,font=20,command=gender)
r3.place(x=0,y=240)

mainloop()


