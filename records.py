from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

window=Tk()
window.title("Hope Hospital")
window.iconbitmap("icon.ico")
window.geometry("700x900+300+0")
window.resizable(False,False)

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

query_btn = Button(text="Show Records", font=("Calibri", 12), command=query)
query_btn.place(x=180, y=575)

delete_box = Entry(window, width=30)
delete_box.place(x=230, y=630)
delete_box_label = Label(window, text="Select ID")
delete_box_label.place(x=180, y=630)

delete_btn = Button(window, text="Delete Record", font=("Calibri", 12), command=delete)
delete_btn.place(x=240, y=660)

def home():
    window.destroy()
    import homepage

back_home=Button(text="Back",command=home)
back_home.place(x=0,y=0)

mainloop()