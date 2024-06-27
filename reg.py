from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title('Patient Registration')
l=Label(window,text="Fill all the details",font = 100)
l.place(x= 250)
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
e1= Entry(window,width=20,font=("Calibri",10))
e1.place(x=100,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
e2 = Entry(window,width=20,font=("Calibri",10))
e2.place(x =100,y=105)

g=Label(text="Choose your gender:",font=50)
g.place(x=0,y=150)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1)
r1.place()
r2=Radiobutton(window,text="Female",variable=var,value=2)
r2.place()
r3=Radiobutton(window,text="Others",variable=var,value=3)
r3.place()

mainloop()


