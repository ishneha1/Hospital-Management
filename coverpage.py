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
    window.configure(bg='#AFEEEE') # background color
    # frame=Frame(window,text="Login",padx=100,pady=100)
    # frame.pack(padx=100,pady=100)
    l2 = Label(window,text="For Patient",bg = '#AFEEEE',fg='black',font=20)
    l2.place(x = 10,y=20)
    l3 = Label(window,text='USER ID:-',bg='#AFEEEE',fg='black')
    l3.place(x=10,y=60)
    e1 = Entry(window,width=20,font=("Calibri",10))
    e1.place(x =100,y=59)
    l4 = Label(window,text='PASSWORD :-',bg= '#AFEEEE',fg ='black')
    l4.place(x =10,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10))
    e2.place(x =100,y=100)
    btn = Button(window,text='LOGIN',bg='white')
    btn.place(x=150,y=155)
    btn1 = Button(text="Create New account",bg='white',command = reg_p)
    btn1.place(x=0,y=155)

    def add():
        if c.get()==0:
            e2.config(show="*")
        else:
            e2.config(show="")
    c=IntVar()
    chk=Checkbutton(text='Show Password',variable=c,bg= '#AFEEEE',command=add)
    chk.place(x=130, y=125)
    
login_page()
    

mainloop()
