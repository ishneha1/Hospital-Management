from tkinter import *
from PIL import Image,ImageTk
cover=Tk()
cover.title("Main Page")
cover.minsize(width=800,height=900)
cover.maxsize(width=1000,height=1300)

hospital=Label(cover,text="HOPE HOSPITAL",font=(UNDERLINE,19))
hospital.pack()
photo1=Image.open("cover.png")
resize_photo1=photo1.resize((200,200))
final_image1=ImageTk.PhotoImage(resize_photo1)
medical_team=Label(cover,image=final_image1,width=0,height=300)
medical_team.place(x=0,y=20)

def Login_page_2():
    cover.destroy()
    global window
    window = Tk()
    window.title("Medical Team login")
    window.geometry('300x200')
    window.configure(bg='#AFEEEE') # background color
    l2 = Label(window,text="Medical Team",bg="#AFEEEE",fg='black',font=20)
    l2.place(x = 10,y=20)
    l3 = Label(window,text='USERNAME:-',bg='#AFEEEE',fg='black')
    l3.place(x=10,y=60)
    e1 = Entry(window,width=20,font=("Calibri",10))
    e1.place(x =100,y=59)
    l4 = Label(window,text='PASSWORD:-',bg= '#AFEEEE',fg ='black')
    l4.place(x =10,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10),show="*")
    e2.place(x =100,y=100)
    btn = Button(window,text='LOGIN',bg='white')
    btn.place(x=95,y=140)
    

    def add():
        if c.get()==0:
            e2.config(show="*")
        else:
            e2.config(show="")
    c=IntVar()
    chk=Checkbutton(text='Show Password',variable=c,command=add)
    chk.place(x=160, y=140)


staff=Button(cover,text="For medical team",font=800,command=Login_page_2)
staff.place(x=20,y=280)


def login_page():
    cover.destroy()
    global window
    window = Tk()
    window.title('Patient login')
    window.geometry('300x200')
    window.configure(bg='#AFEEEE') # background color
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
    chk=Checkbutton(text='Show Password',variable=c,command=add)
    chk.place(x=130, y=125)

    
def reg_p():
    window.destroy()
    import reg


photo2=Image.open("cover2.png")
resize_photo2=photo2.resize((200,200))
final_image2=ImageTk.PhotoImage(resize_photo2)
patient_team=Label(cover,image=final_image2,width=0,height=300)
patient_team.place(x=500,y=20)

patient=Button(cover,text="For patient",font=800,command=login_page)
patient.place(x=550,y=280)

mainloop()
