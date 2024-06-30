from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title('Patient Registration')

window.minsize(height=700,width=800)
window.maxsize(height=700,width=800)

l=Label(window,text="Fill all the details.",font = 100)
l.pack()
l1 = Label(window,text="First Name",font=50)
l1.place(x=0,y=50)
e1= Entry(window,width=20,font=("Calibri",10))
e1.place(x=120,y=54)
l2 = Label(window,text="Last Name",font = 50)
l2.place(x=0,y=100)
e2 = Entry(window,width=20,font=("Calibri",10))
e2.place(x =120,y=105)
l3= Label(window,text="Age",font=50)
l3.place(x=0,y=150)
e3= Entry(window,width=20,font=("Calibri",10))
e3.place(x=120,y=150)
l4= Label(window,text="Blood Group",font=50)
l4.place(x=0,y=200)
e4= Entry(window,width=20,font=("Calibri",10))
e4.place(x=120,y=205)
l5= Label(window,text="Contact",font=50)
l5.place(x=0,y=250)
e5= Entry(window,width=20,font=("Calibri",10))
e5.place(x=120,y=255)
l6= Label(window,text="Email",font=50)
l6.place(x=0,y=300)
e6= Entry(window,width=20,font=("Calibri",10))
e6.place(x=120,y=305)
b1=Button(text='Submit',font=("Calibri",12))
b1.place(x=205,y=455)


def gender():
    text=var.get()


g=Label(text="Gender:",font=("Arial Bold",15))
g.place(x=0,y=350)
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,font=20,value=1,command=gender)
r1.place(x=0,y=380)
r2=Radiobutton(window,text="Female",variable=var,value=2,font=20,command=gender)
r2.place(x=0,y=410)
r3=Radiobutton(window,text="Others",variable=var,value=3,font=20,command=gender)
r3.place(x=0,y=440)

photo2=Image.open("o4.png")
resize_photo2=photo2.resize((500,500))
final_image2=ImageTk.PhotoImage(resize_photo2)
picture=Label(window, image=final_image2, width=0, height=600)
picture.pack(side=RIGHT)

mainloop()


