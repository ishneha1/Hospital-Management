from tkinter import *
from tkinter import messagebox
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

    if record_id:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        # Searching for the record by ID
        cursor.execute("SELECT * FROM patients WHERE id=?", (record_id,))
        record = cursor.fetchone()
        conn.close()

        if record:
            listbox.delete(0, END)
            listbox.insert(END, record)
        else:
            messagebox.showwarning("Warning", f"No record found with ID {record_id}.")
    else:
        messagebox.showwarning("Warning", "Please enter an ID to search.")

# Function to delete the selected record
def delete_record():
    selected_record = listbox.curselection()

    if selected_record:
        record = listbox.get(selected_record)
        record_id = record[0]

        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        # Deleting the record with the selected ID
        cursor.execute("DELETE FROM patients WHERE id=?", (record_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Record ID {record_id} deleted successfully!")
        listbox.delete(0, END)  # Clear the listbox after deletion
    else:
        messagebox.showwarning("Warning", "Please select a record to delete.")


# Creating label and entry to input the record ID
Label(window, text="Enter Record ID:").grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(window)
entry_id.grid(row=0, column=1, padx=10, pady=10)

# Button to search for the record
search_button = Button(window text="Search Record", command=search_record)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Creating a Listbox to display the specific record
listbox = Listbox(window, width=100, height=10)
listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Button to delete the selected record
delete_button = Button(window, text="Delete Record", command=delete_record)
delete_button.grid(row=2, column=1, pady=10)

window.mainloop()