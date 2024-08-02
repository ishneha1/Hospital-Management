from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Hope Hospital")
# window.iconbitmap("icon.ico")
window.minsize(height=900, width=700)
window.maxsize(height=900, width=700)

conn = sqlite3.connect("hospital.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS patients (
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
    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO patients VALUES (:first, :last, :age, :address, :blood, :contact, :email, :password, :confirm, :gender)",
        {
            "first": f_name.get(),
            "last": l_name.get(),
            "age": age.get(),
            "address": address.get(),
            "blood": blood_group.get(),
            "contact": contact.get(),
            "email": email.get(),
            "password": password.get(),
            "confirm": confirm_password.get(),
            "gender": selected_option.get()
        }
    )
    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    blood_group.delete(0, END)
    contact.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    confirm_password.delete(0, END)
    messagebox.showinfo("Success", "Record Added Successfully")
    window.destroy()
    import homepage


def query():
    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM patients")
    records = c.fetchall()
    conn.commit()
    conn.close()

    display_records = ""
    for record in records:
        display_records += f"ID {record[-1]}: {record[0]} {record[1]}, Age: {record[2]}, Address: {record[3]}, Blood_group: {record[4]}, Contact: {record[5]}, Email:{record[6]}, Password:{record[7]}, Confirm_password:{record[8]}, Gender:{record[9]}\n"
    query_label = Label(window, text=display_records)
    query_label.place(x=50, y=700)


def delete():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("DELETE from patients WHERE oid=" + delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0, END)
    messagebox.showinfo("Success", "Record Deleted Successfully")


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
age = Entry(window, width=25, font=("Calibri", 10))
age.place(x=180, y=150)
adress_label = Label(window, text="Address", font=50)
adress_label.place(x=0, y=200)
address = Entry(window, width=25, font=("Calibri", 10))
address.place(x=180, y=200)
blood_group_label = Label(window, text="Blood Group", font=50)
blood_group_label.place(x=0, y=250)
blood_group = Entry(window, width=25, font=("Calibri", 10))
blood_group.place(x=180, y=255)
contact_label = Label(window, text="Contact", font=50)
contact_label.place(x=0, y=300)
contact = Entry(window, width=25, font=("Calibri", 10))
contact.place(x=180, y=305)
email_label = Label(window, text="Email", font=50)
email_label.place(x=0, y=350)
email = Entry(window, width=25, font=("Calibri", 10))
email.place(x=180, y=355)
submit_button = Button(text="Submit", font=("Calibri", 12), command=submitted)
submit_button.place(x=180, y=520)
query_btn = Button(text="Show Records", font=("Calibri", 12), command=query)
query_btn.place(x=180, y=575)

password_label = Label(window, text="Password", font=50)
password_label.place(x=0, y=400)
password = Entry(window, width=25, font=("Calibri", 10),show='*')
password.place(x=180, y=402)
confirm_password_label = Label(window, text="Confrim Password", font=20)
confirm_password_label.place(x=0, y=460)
confirm_password = Entry(window, width=25, font=("Calibri", 10),show='*')
confirm_password.place(x=180, y=460)
def toggle_password():
        if show_pass_var.get():
            password.config(show="")
        else:
            password.config(show="*")
        if show_pass_var.get():
            confirm_password.config(show="")
        else:
            confirm_password.config(show="*")
    
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

delete_box = Entry(window, width=30)
delete_box.place(x=230, y=630)
delete_box_label = Label(window, text="Select ID")
delete_box_label.place(x=180, y=630)

delete_btn = Button(window, text="Delete Record", font=("Calibri", 12), command=delete)
delete_btn.place(x=240, y=660)

photo2=Image.open("o4.png")
resize_photo2 = photo2.resize((400, 500))
final_image2 = ImageTk.PhotoImage(resize_photo2)
picture = Label(window, image=final_image2, width=0, height=600)
picture.place(x=390, y=40)


mainloop()