from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.minsize(height=900,width=700)
root.maxsize(height=900,width=700)

image_0 = Image.open('back.jpg')
image_0 = image_0.resize((700, 900), Image.LANCZOS)
bck_end = ImageTk.PhotoImage(image_0)

# Create a canvas to hold the background image and the text
canvas = Canvas(root, width=200, height=800)
canvas.pack(fill="both", expand=True)

# Display the background image
canvas.create_image(350, 450, image=bck_end, anchor="center")

#for importing info
def information():
    root.destroy()
    root1= Tk()
    root1.title("Hope Hospital")
    root1.iconbitmap('icon.ico')
    root1.minsize(height=900,width=700)
    root1.maxsize(height=900,width=700)
    image_0 = Image.open('abs.jpeg')
    image_0 = image_0.resize((700, 900), Image.LANCZOS)
    bck_end = ImageTk.PhotoImage(image_0)

    # Create a canvas to hold the background image and the text
    canvas = Canvas(root1, width=200, height=800)
    canvas.pack(fill="both", expand=True)

    # Display the background image
    canvas.create_image(350, 450, image=bck_end, anchor="center")

    # Create a Text widget to display the paragraph
    text_widget = Text(root1, wrap=WORD, width=50, height=10)
    text_widget.pack(padx=10, pady=90)


    # Define the paragraph text
    paragraph = """Welcome to our  Hope Hospital Management System.
    This system is designed to streamline the administrative and clinical processes
    of hospitals and healthcare facilities. With our system, you can efficiently
    manage patient records, staff schedules, book an appointment and much more.
    Experience a new level of efficiency and care with our innovative solution."""

    # Add the paragraph text to the Canvas
    canvas.create_text(370, 350, text=paragraph, fill="black", font=("Arial", 16), width=500,state=DISABLED)

    mainloop()


#for information icon
info=Label(root,text="About us",font=("Helvetica", 20),bg="#E8FCF8")
info.place(x=0,y=120)
info_pic=Image.open("home.ico")
resize_info_pic=info_pic.resize((40,60))
final_info_image=ImageTk.PhotoImage(resize_info_pic)
info_icon=Button(root, image=final_info_image, width=0, height=0,command=information)
info_icon.place(x=35,y=50)

#import dashboard
def doc():
    root.destroy()
    import dashboard

#for doctors
doctor=Label(root,text="Our Doctors",font=("Helvetica", 20),bg="#E8FCF8")
doctor.place(x=250,y=120)
doctor_pic=Image.open("doc.ico")
resize_doc_pic=doctor_pic.resize((40,60))
final_doc_image=ImageTk.PhotoImage(resize_doc_pic)
doc_icon=Button(root,image=final_doc_image,width=0,height=0,command=doc)
doc_icon.place(x=300,y=50)



mainloop()