from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.minsize(height=900,width=700)
root.maxsize(height=900,width=700)
image_0 = Image.open('abs.jpeg')
image_0 = image_0.resize((700, 900), Image.LANCZOS)
bck_end = ImageTk.PhotoImage(image_0)

# Create a canvas to hold the background image and the text
canvas = Canvas(root, width=200, height=800)
canvas.pack(fill="both", expand=True)

# Display the background image
canvas.create_image(350, 450, image=bck_end, anchor="center")

# Create a Text widget to display the paragraph
text_widget = Text(root, wrap=WORD, width=50, height=10)
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