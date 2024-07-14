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

doc_name=Label(root,text="Doctors",font=("Arial Bold",16), justify="left")
doc_name.pack(padx=10,pady=10,anchor="w")

# img 1
image = Image.open('./assets/image/doctor1.png')
img_size=image.resize((100,100))
image = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(root, image=image, justify="left")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(root,text="Manish Rumba",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(root,text="Dentist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


button1=Button(root,text="Make an Appointment", justify="left")
button1.pack(padx=10,pady=30,anchor="w")

# img 2
image = Image.open('./assets/image/doctor2.jpg')
img_size=image.resize((150,150))
image = ImageTk.PhotoImage(img_size)

# Create a label to display the image
image_label = Label(root, image=image, justify="left")
image_label.pack(padx=0, pady=0, anchor="w")
doc_name=Label(root,text="Manish rumba",font=("Arial",14), justify="right")
doc_name.pack(padx=10,pady=10,anchor="w")
doc_specilist=Label(root,text="Dentist",font=("Arial",12), justify="left")
doc_specilist.pack(padx=10,pady=0,anchor="w")


button1=Button(root,text="Make an Appointment", justify="left")
button1.pack(padx=10,pady=0,anchor="w")


mainloop()
