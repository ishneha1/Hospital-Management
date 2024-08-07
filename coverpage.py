from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox

def logged():
    window.destroy()
    import homepage
  
# Show/hide password checkbox
def toggle_password():
        if show_pass_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")
     

#login page 
window = Tk()
window.title('Hope Hospital')
window.iconbitmap("icon.ico")
window.geometry("700x900+300+0")
window.resizable(False,False)

# Load the background image
image = Image.open("coverpage.png")
bg_image = ImageTk.PhotoImage(image)

# Create a Canvas widget
canvas = Canvas(width=700, height=900)
canvas.pack(fill="both", expand=True)

# Set the image on the Canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")


# Main frame
frame1 = Frame(window, highlightbackground="#333", highlightthickness=1)
frame1_window=canvas.create_window(215, 550, anchor="nw", window=frame1)

#additional frame
frame2 = Frame(window,highlightbackground="#333",highlightthickness=1)
frame2.pack(padx=650,pady=280)
title=Label(frame2,text="Hope Hospital",font=("Arial Bold",12))
title.place(x=120,y=90,anchor=E)
logo=Image.open("icon.ico")
logo_resize=logo.resize((60,60))
final_logo=ImageTk.PhotoImage(logo_resize)
logo_label=Label(frame2,image=final_logo)
logo_label.place(x=100,y=100)

# User ID
Label(frame1, text="FULL NAME:", fg="black").grid(row=0, column=0, sticky=W, padx=10, pady=10)
user_id_entry = Entry(frame1, width=20, font=("Calibri", 12))
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

# Password
Label(frame1, text="PASSWORD:", fg="black").grid(row=1, column=0, sticky=W, padx=10, pady=10)
password_entry = Entry(frame1, width=20, font=("Calibri", 12), show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)


    
show_pass_var = IntVar()
Checkbutton(frame1, text="Show Password", variable=show_pass_var, command=toggle_password).grid(row=2, column=1, sticky=W)


# Login button
Button(frame1, text="LOGIN", bg="white",command=logged).grid(row=3, column=1, pady=20)


mainloop()
