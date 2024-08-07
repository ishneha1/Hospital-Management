from tkinter import *
from tkinter import messagebox
import sqlite3

root= Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.geometry("700x900+300+0")
root.resizable(False,False)

# Function to search and display a specific record by ID
def search_record():
    record_id = entry_id.get()

    if record_id:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        # Searching for the record by ID
        cursor.execute("SELECT * FROM patients WHERE id=?", (record_id))
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
Label(root, text="Enter Record ID:").grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=10)

# Button to search for the record
search_button = Button(root, text="Search Record", command=search_record)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Creating a Listbox to display the specific record
listbox = Listbox(root, width=100, height=10)
listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Button to delete the selected record
delete_button = Button(root, text="Delete Record", command=delete_record)
delete_button.grid(row=2, column=1, pady=10)

root.mainloop()