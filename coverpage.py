from tkinter import *
from PIL import Image,ImageTk

def reg_p():
    window.destroy()
    import reg


def login_page():
    global window
    window = Tk()
    window.title('Hope Hospital')
    window.iconbitmap("icon.ico")
    window.minsize(height=900,width=700)
    window.maxsize(height=900,width=700)
    #window.resizable(0,0)
    # window.configure(bg='#AFEEEE') # background color
    frame1 = Frame(window, highlightbackground="#333", highlightthickness=1)
    frame1.pack(padx=0, pady=50)
    l3 = Label(frame1,text='USER ID:-',fg='black')
    l3.place(x=100,y=60)
    e1 = Entry(window,width=20,font=("Calibri",10))
    e1.place(x =100,y=59)
    l4 = Label(window,text='PASSWORD :-',fg ='black')
    l4.place(x =100,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10))
    e2.place(x =100,y=100)
    btn = Button(window,text='LOGIN',bg='white')
    btn.place(x=198,y=125)


    def add():
        if c.get()==0:
            e2.config(show="*")
        else:
            e2.config(show="")
    c=IntVar()
    chk=Checkbutton(frame1,text='Show Password',variable=c,command=add)
    chk.place(x=0, y=125)
    
login_page()
    

mainloop()
