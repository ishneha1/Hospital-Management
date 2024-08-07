from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Hope Hospital")
window.iconbitmap("icon.ico")
window.minsize(height=900, width=700)
window.maxsize(height=900, width=700)

conn = sqlite3.connect("hospital.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name text,
            last_name text,
            age integer,
            address text,
            blood_group text,
            contact integer,
            email text,
            password text,
            confirm_password text,
            gender text
            )"""
)
conn.commit()
conn.close()


def submitted():
    first_name = f_name.get()
    last_name = l_name.get()
    age = entry_age.get()
    address = entry_address.get()
    blood_group = entry_blood_group.get()
    contact = entry_contact.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password= entry_confirm_password.get()
    gender= selected_option.get()
    if not all([first_name, last_name, age, address, blood_group, contact, email, password, confirm_password, gender]):
        messagebox.showwarning("Warning", "Please fill in all the fields.")
    else:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO patients (first_name, last_name, age, address, blood_group, contact, email, password, confirm_password, gender)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, age, address, blood_group, contact, email, password, confirm_password, gender))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Record Added Successfully")
        window.destroy()
        import homepage

    
    f_name.delete(0, END)
    l_name.delete(0, END)
    entry_age.delete(0, END)
    entry_address.delete(0, END)
    entry_blood_group.delete(0, END)
    entry_contact.delete(0, END)
    entry_email.delete(0, END)
    entry_password.delete(0, END)
    



l = Label(window, text="Fill all the details.", font=("Arial Bold", 20))
l.pack()
f_name_label = Label(window, text="First Name", font=50)
f_name_label.place(x=0, y=50)
f_name = Entry(window, width=25, font=("Calibri", 10))
f_name.place(x=180, y=54)
l_name_label = Label(window, text="Last Name", font=50)
l_name_label.place(x=0, y=100)
l_name = Entry(window, width=25, font=("Calibri", 10))
l_name.place(x=180, y=105)
age_label = Label(window, text="Age", font=50)
age_label.place(x=0, y=150)
entry_age = Entry(window, width=25, font=("Calibri", 10))
entry_age.place(x=180, y=150)
adress_label = Label(window, text="Address", font=50)
adress_label.place(x=0, y=200)
entry_address = Entry(window, width=25, font=("Calibri", 10))
entry_address.place(x=180, y=200)
blood_group_label = Label(window, text="Blood Group", font=50)
blood_group_label.place(x=0, y=250)
entry_blood_group = Entry(window, width=25, font=("Calibri", 10))
entry_blood_group.place(x=180, y=255)
contact_label = Label(window, text="Contact", font=50)
contact_label.place(x=0, y=300)
entry_contact = Entry(window, width=25, font=("Calibri", 10))
entry_contact.place(x=180, y=305)
email_label = Label(window, text="Email", font=50)
email_label.place(x=0, y=350)
entry_email = Entry(window, width=25, font=("Calibri", 10))
entry_email.place(x=180, y=355)
submit_button = Button(text="Submit", font=("Calibri", 12), command=submitted)
submit_button.place(x=330, y=630)


password_label = Label(window, text="Password", font=50)
password_label.place(x=0, y=400)
entry_password = Entry(window, width=25, font=("Calibri", 10),show='*')
entry_password.place(x=180, y=402)
confirm_password_label = Label(window, text="Confrim Password", font=20)
confirm_password_label.place(x=0, y=460)
entry_confirm_password = Entry(window, width=25, font=("Calibri", 10),show='*')
entry_confirm_password.place(x=180, y=460)
def toggle_password():
        if show_pass_var.get():
            entry_password.config(show="")
        else:
            entry_password.config(show="*")
        if show_pass_var.get():
            entry_confirm_password.config(show="")
        else:
            entry_confirm_password.config(show="*")
    
show_pass_var = IntVar()
Checkbutton(text="Show Password", variable=show_pass_var, command=toggle_password).place(x=270, y=500)





gender_label = Label(text="Gender:", font=("Arial Bold", 15))
gender_label.place(x=0, y=545)

selected_option= StringVar(value="Male")
r1 = Radiobutton(window, text="Male", variable=selected_option, font=20, value="Male")
r1.place(x=0, y=585)
r2 = Radiobutton(window, text="Female", variable=selected_option, value="Female", font=20)
r2.place(x=0, y=610)
r3 = Radiobutton(window, text="Others", variable=selected_option, value="Others", font=20)
r3.place(x=0, y=635)



photo2=Image.open("o4.png")
resize_photo2 = photo2.resize((400, 500))
final_image2 = ImageTk.PhotoImage(resize_photo2)
picture = Label(window, image=final_image2, width=0, height=600)
picture.place(x=390, y=40)


mainloop()