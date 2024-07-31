from tkinter import *
from PIL import Image,ImageTk

#importing reg page 
def reg_p():
    window.destroy()
    import reg

#login page 
window = Tk()
window.title('Hope Hospital')
window.iconbitmap("icon.ico")
window.minsize(height=900,width=700)
window.maxsize(height=900,width=700)

# Main frame
frame1 = Frame(window, highlightbackground="#333", highlightthickness=1)
frame1.pack(padx=0, pady=290)

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
Label(frame1, text="USER ID:", fg="black").grid(row=0, column=0, sticky=W, padx=10, pady=10)
user_id_entry = Entry(frame1, width=20, font=("Calibri", 12))
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

# Password
Label(frame1, text="PASSWORD:", fg="black").grid(row=1, column=0, sticky=W, padx=10, pady=10)
password_entry = Entry(frame1, width=20, font=("Calibri", 12), show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Show/hide password checkbox
def toggle_password():
        if show_pass_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")
    
show_pass_var = IntVar()
Checkbutton(frame1, text="Show Password", variable=show_pass_var, command=toggle_password).grid(row=2, column=1, sticky=W)

def logged():
     window.destroy()
     import homepage
     
# Login button
Button(frame1, text="LOGIN", bg="white",command=logged).grid(row=3, column=1, pady=20)

mainloop()
