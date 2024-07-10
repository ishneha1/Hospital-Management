from tkinter import *
from PIL import Image,ImageTk

# Create the main window
root =Tk()
root.title("Background Image Example")

# Load the image file using one of the corrected path methods
bg_image = Image.open("hospitalpage1.jpg")

  # Use the correct path format


# Create a Label widget with the background image
bg_label =Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Optionally, add more widgets over the Label
label =Label(root, text="Hello, World!", font=("Arial", 20), bg='white')
label.place(x=50, y=50)  # Position the label

# Start the main event loop
root.mainloop()
