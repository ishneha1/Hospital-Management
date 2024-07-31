import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert a sample user (username: user, password: pass)
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user', 'pass')")

# Commit changes and close the connection
conn.commit()
conn.close()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Execute SQL query to check if the user exists
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        show_welcome_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to show the welcome window
def show_welcome_window(username):
    login_window.withdraw()  # Hide the login window

    welcome_window = tk.Toplevel()
    welcome_window.title("Welcome")
    
    welcome_label = tk.Label(welcome_window, text=f"Welcome, {username}!")
    welcome_label.pack(pady=20)

    close_button = tk.Button(welcome_window, text="Close", command=welcome_window.destroy)
    close_button.pack(pady=10)

# Create the main login window
login_window = tk.Tk()
login_window.title("Login")

username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=20)

login_window.mainloop()