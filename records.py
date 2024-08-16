from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.geometry("700x900+300+0")
root.resizable(False, False)

# Function to search and display a specific record by ID
def search_record():
    record_id = entry_id.get()

    if record_id:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        # Searching for the record by ID
        cursor.execute("SELECT * FROM patients WHERE id=?", (record_id,))
        record = cursor.fetchone()
        conn.close()

        if record:
            entry_fname.delete(0, END)
            entry_lname.delete(0, END)
            entry_age.delete(0, END)
            entry_address.delete(0, END)
            entry_blood_group.delete(0, END)
            entry_contact.delete(0, END)
            entry_email.delete(0, END)

            entry_fname.insert(END, record[1])
            entry_lname.insert(END, record[2])
            entry_age.insert(END, record[3])
            entry_address.insert(END, record[4])
            entry_blood_group.insert(END, record[5])
            entry_contact.insert(END, record[6])
            entry_email.insert(END, record[7])
        else:
            messagebox.showwarning("Warning", f"No record found with ID {record_id}.")
    else:
        messagebox.showwarning("Warning", "Please enter an ID to search.")

# Function to update the selected record
def update_record():
    record_id = entry_id.get()

    if record_id:
        fname = entry_fname.get()
        lname = entry_lname.get()
        age = entry_age.get()
        address = entry_address.get()
        blood_group = entry_blood_group.get()
        contact = entry_contact.get()
        email = entry_email.get()

        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        # Updating the record with the new values
        cursor.execute("""
            UPDATE patients SET
            first_name=?, last_name=?, age=?, address=?, blood_group=?, contact=?, email=?
            WHERE id=?""",
            (fname, lname, age, address, blood_group, contact, email, record_id)
        )
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Record ID {record_id} updated successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter an ID to update.")

# Creating label and entry to input the record ID
Label(root, text="Enter Record ID:").grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=10)

# Button to search for the record
search_button = Button(root, text="Search Record", command=search_record)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Fields to display and update the record details
Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=10)
entry_fname = Entry(root)
entry_fname.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=10)
entry_lname = Entry(root)
entry_lname.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Age:").grid(row=3, column=0, padx=10, pady=10)
entry_age = Entry(root)
entry_age.grid(row=3, column=1, padx=10, pady=10)

Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=10)
entry_address = Entry(root)
entry_address.grid(row=4, column=1, padx=10, pady=10)

Label(root, text="Blood Group:").grid(row=5, column=0, padx=10, pady=10)
entry_blood_group = Entry(root)
entry_blood_group.grid(row=5, column=1, padx=10, pady=10)

Label(root, text="Contact:").grid(row=6, column=0, padx=10, pady=10)
entry_contact = Entry(root)
entry_contact.grid(row=6, column=1, padx=10, pady=10)

Label(root, text="Email:").grid(row=7, column=0, padx=10, pady=10)
entry_email = Entry(root)
entry_email.grid(row=7, column=1, padx=10, pady=10)

# Button to update the record
update_button = Button(root, text="Update Record", command=update_record)
update_button.grid(row=8, column=1, pady=20)

root.mainloop()