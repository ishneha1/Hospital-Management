from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Hope Hospital")
root.iconbitmap("icon.ico")
root.geometry("700x900+300+0")
root.resizable(False,False)
hospital=Label(root,text="Hope Hospital",font=("Arial Bold",10))
hospital.pack()

# Doctor Lists
doctors=Label(root,text="Our Doctors",font=("Arial Bold",30))
doctors.pack(padx=0,pady=0,anchor="center")


# frame
frame1 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame1.place(x=252,y=125) 
# img 1
image = Image.open('doctor1.png')
img_size=image.resize((150,150))
image = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(frame1, image=image, justify="left")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(frame1,text="Manish Rumba",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame1,text="Dentist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")



#fame2
frame2 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame2.place(x=252,y=445)


# img 2
image2 = Image.open('doctor2.jpg')
img_size=image2.resize((150,150))
image2 = ImageTk.PhotoImage(img_size)
 
# Create a label to display the image
image_label = Label(frame2, image=image2, justify="center")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(frame2,text="Ishneha Hirachan",font=("Arial",14), justify="right")
doc_name.pack(padx=0,pady=10,anchor="w")
doc_specilist=Label(frame2,text="Cardiology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


#frame3
frame3 = Frame(root, highlightbackground="#333", highlightthickness=1)
frame3.place(x=10, y=125, anchor="nw")

# img 3
image3 = Image.open('doctor3.png')
img_size=image3.resize((150,150))
image3 = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(frame3, image=image3, justify="center")
image_label.pack(padx=0, pady=0, anchor="nw")
doc_name=Label(frame3,text="Simon Rai",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame3,text="Neurosurgery",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="nw")


#frame4

frame4 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame4.place(x=10,y=560,anchor="w")

#img4
image4=Image.open('doctor4.png')
img_size=image4.resize((150,150))
image4 = ImageTk.PhotoImage(img_size)

#create a label to display the image
image_label = Label(frame4, image=image4, justify="center")
image_label.pack(padx=0, pady=0, anchor="nw")
doc_name=Label(frame4,text="Saroj Thapa",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame4,text="Nephrology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="nw")


#frame5

frame5 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame5.place(x=650,y=240,anchor="e")

#img5
image5=Image.open('doctor5.png')
img_size=image5.resize((150,150))
image5 = ImageTk.PhotoImage(img_size)

#create a label to display the image/
image_label = Label(frame5, image=image5, justify="center")
image_label.pack(padx=0, pady=0, anchor="e")
doc_name=Label(frame5,text="Katrina Kaif",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame5,text="Gynecologist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")

#frame6

frame6 = Frame(root,highlightbackground="#333",highlightthickness=1)
frame6.place(x=650,y=560,anchor="e")

#img6
image6=Image.open('doctor6.png')
img_size=image6.resize((150,150))
image6 = ImageTk.PhotoImage(img_size)

#create a label to display the image
image_label = Label(frame6, image=image6, justify="center")
image_label.pack(padx=0, pady=0, anchor="e")
doc_name=Label(frame6,text="Ronaldo Pun",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(frame6,text="Hematology",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")

def home():
    root.destroy()
    import homepage

back_home=Button(text="Back",command=home)
back_home.place(x=0,y=0)

mainloop()
