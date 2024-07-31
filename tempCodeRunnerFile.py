def toggle_password():
        if show_pass_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")
    
show_pass_var = IntVar()
Checkbutton(frame1, text="Show Password", variable=show_pass_var, command=toggle_password).grid(row=2, column=1, sticky=W)