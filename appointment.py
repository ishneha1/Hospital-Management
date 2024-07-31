from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            doctor TEXT,
            date TEXT,
            patient TEXT
        )
    ''')
conn.commit()


def clear_entries():
    date_entry.delete(0, END)
    patient_entry.delete(0, END)


def book_appointment():
    doctor = doctor_var.get()
    date = date_entry.get()
    patient = patient_entry.get()

    if not date or not patient:
        messagebox.showwarning("Input Error", "Please enter all fields.")
        return
    
    cursor.execute('''
        INSERT INTO appointments (doctor, date, patient)
        VALUES (?, ?, ?)
    ''', (doctor, date, patient))
    conn.commit()
    
    messagebox.showinfo("Appointment Booked", f"Appointment booked with {doctor} on {date} for {patient}")
    clear_entries()


def view_appointments():
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    
    if not appointments:
        messagebox.showinfo("No Appointments", "No appointments booked yet.")
        return
    
    appointments_window = Toplevel(root)
    appointments_window.title("View Appointments")
    appointments_window.geometry("400x300")
    
    appointments_listbox = Listbox(appointments_window, width=50, height=15)
    appointments_listbox.pack(pady=10)
    
    for appointment in appointments:
        appointments_listbox.insert(END, f"ID: {appointment[0]} | Doctor: {appointment[1]} | Date: {appointment[2]} | Patient: {appointment[3]}")


root.title("Doctor Appointment Booking System")
root.geometry("400x400")

label_heading = Label(root, text="Book an Appointment", font=("Arial", 16))
label_heading.pack(pady=10)

label_doctor = Label(root, text="Select Doctor:")
label_doctor.pack(pady=5)

doctors = ['Dr. Manish Rumba', 'Dr. Saroj Thapa', 'Dr. Katrina Kaif', 'Dr. Ishneha Hirachan', 'Dr. Simon Rai', 'Dr. Ronaldo Pun'] 
doctor_var = StringVar(root)
doctor_var.set(doctors[0])  
doctor_menu = ttk.Combobox(root, textvariable=doctor_var, values=doctors, state='readonly')
doctor_menu.pack(pady=5)

label_date = Label(root, text="Select Date (YYYY-MM-DD):")
label_date.pack(pady=5)

date_entry = Entry(root)
date_entry.pack(pady=5)

label_patient = Label(root, text="Enter Patient Name:")
label_patient.pack(pady=5)

patient_entry = Entry(root)
patient_entry.pack(pady=5)

submit_button = Button(root, text="Book Appointment", command=book_appointment)
submit_button.pack(pady=10)

view_button = Button(root, text="View Appointments", command=view_appointments)
view_button.pack(pady=10)




root.mainloop()


conn.close()
