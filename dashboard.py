from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Hope Hospital")
root.iconbitmap("icon.ico")
root.minsize(height=900,width=700)
root.maxsize(height=900,width=700)
#root.resizable(0,0)
hospital=Label(root,text="Dashboard",font=("Arial Bold",10))
hospital.pack()

# Doctor Lists
doctors=Label(root,text="Doctors List",font=("Arial Bold",30))
doctors.pack(padx=0,pady=0,anchor="center")


#NEW window
def new_window():
    root.destroy()
    import appointment
    
# frame
frame1 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame1.pack(padx=0, pady=50)
# img 1
image = Image.open('./assets/image/doctor1.png')
img_size=image.resize((150,150))
image = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(frame1, image=image, justify="left")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(frame1,text="Manish Rumba",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame1,text="Dentist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


button1=Button(frame1,text="Make an Appointment", justify="left",command=new_window)
button1.pack(padx=10,pady=30,anchor="w")

#fame2
frame2 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame2.place(x=272,y=450)


# img 2
image2 = Image.open('./assets/image/doctor2.jpg')
img_size=image2.resize((150,150))
image2 = ImageTk.PhotoImage(img_size)
 
# Create a label to display the image
image_label = Label(frame2, image=image2, justify="center")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(frame2,text="Ishneha Hirachan",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame2,text="Cardiology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


button2=Button(frame2,text="Make an Appointment", justify="left",command=new_window)
button2.pack(padx=10,pady=30,anchor="w")



#frame3
frame3 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame3.place(x=10, y=125, anchor="nw")

# img 3
image3 = Image.open('./assets/image/doctor3.png')
img_size=image3.resize((150,150))
image3 = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(frame3, image=image3, justify="center")
image_label.pack(padx=0, pady=0, anchor="nw")
doc_name=Label(frame3,text="Simon Rai",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame3,text="Neurosurgery",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="nw")


button3=Button(frame3,text="Make an Appointment", justify="left",command=new_window)
button3.pack(padx=10,pady=30,anchor="nw")


#frame4

frame4 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame4.place(x=10,y=605,anchor="w")

#img4
image4=Image.open('./assets/image/doctor4.png')
img_size=image4.resize((150,150))
image4 = ImageTk.PhotoImage(img_size)

#create a label to display the image
image_label = Label(frame4, image=image4, justify="center")
image_label.pack(padx=0, pady=0, anchor="nw")
doc_name=Label(frame4,text="Saroj Thapa",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame4,text="Nephrology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="nw")


button4=Button(frame4,text="Make an Appointment", justify="left",command=new_window)
button4.pack(padx=10,pady=30,anchor="nw")




#frame5

frame5 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame5.place(x=650,y=280,anchor="e")

#img5
image5=Image.open('./assets/image/doctor5.png')
img_size=image5.resize((150,150))
image5 = ImageTk.PhotoImage(img_size)

#create a label to display the image
image_label = Label(frame5, image=image5, justify="center")
image_label.pack(padx=0, pady=0, anchor="e")
doc_name=Label(frame5,text="David Kaif",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame5,text="Gynecologist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


button5=Button(frame5,text="Make an Appointment", justify="left",command=new_window)
button5.pack(padx=10,pady=30,anchor="e")



#frame6

frame6 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame6.place(x=650,y=605,anchor="e")

#img6
image6=Image.open('./assets/image/doctor6.png')
img_size=image6.resize((150,150))
image6 = ImageTk.PhotoImage(img_size)

#create a label to display the image
image_label = Label(frame6, image=image6, justify="center")
image_label.pack(padx=0, pady=0, anchor="e")
doc_name=Label(frame6,text="Ronaldo Pun",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame6,text="Hematology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")



button6=Button(frame6,text="Make an Appointment", justify="left",command=new_window)
button6.pack(padx=10,pady=30,anchor="e")






   




root.mainloop()
