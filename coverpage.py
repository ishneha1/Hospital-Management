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
    
# #homepage after logging in 
# def logged_in():
#       window.destroy()
#       import homepage

# l3 = Label(window,text='USER ID:-',fg='black')
# l3.place(x=0,y=60)
# e1 = Entry(window,width=20,font=("Calibri",10))
# e1.place(x =100,y=59)
# l4 = Label(window,text='PASSWORD :-',fg ='black')
# l4.place(x =0,y=100)
# e2 = Entry(window,width=20,font=("Calibri",10))
# e2.place(x =100,y=100)
# btn = Button(window,text='LOGIN',bg='white',command=logged_in)
# btn.place(x=198,y=125)


# def add():
#     if c.get()==0:
#             e2.config(show="*")
#     else:
#             e2.config(show="")
# c=IntVar()
# chk=Checkbutton(window,text='Show Password',variable=c,command=add)
# chk.place(x=0, y=125)
    
# Main frame
frame1 = Frame(window, highlightbackground="#333", highlightthickness=1)
frame1.pack(padx=00, pady=290)

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

# Login button
Button(frame1, text="LOGIN", bg="white").grid(row=3, column=1, pady=20)

mainloop()
