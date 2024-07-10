from tkinter import *
from PIL import ImageTk, Image

# Initialize the main application window
root = Tk()
root.title("Project..")

# Open and resize the image
image_0 = Image.open('hospitalpage1.jpg')
image_0 = image_0.resize((900, 700), Image.LANCZOS)
bck_end = ImageTk.PhotoImage(image_0)

# Set window geometry
root.geometry('900x700')

# Create a canvas to hold the background image and the text
canvas = Canvas(root, width=200, height=800)
canvas.pack(fill="both", expand=True)

# Display the background image
canvas.create_image(450, 350, image=bck_end, anchor="center")


# Function to change text color when clicked
def change_color(event):
    canvas.itemconfig(clickable_text, fill="red")


# Create clickable text on the canvas with a transparent background
clickable_text = canvas.create_text(620, 632, text="Sign In",
                                    font=("Helvetica", 16), fill="black", justify='center')

# Bind a mouse click event to the text
canvas.tag_bind(clickable_text, "<Button-1>", change_color)




#Add a button with specified text and styles
button1 = Button(root, text="REGISTER", font=("Helvetica",10) ,fg="white", bg="red", padx=80, pady=10)
button1.place(x=360, y=550)


# Create text on the canvas with a transparent background
canvas.create_text(470, 500, text="Health is Not Valued \n Until Sickness Comes",
                   font=("Helvetica", 22), fill="black", justify='center')

canvas.create_text(460,632,text="Already have a account ?",font=("Helvetica",16),fill="black"
                   ,justify="center")                            





root.mainloop()
