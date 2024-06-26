from tkinter import *
from PIL import Image,ImageTk
cover=Tk()
cover.title("page")
cover.minsize(width=800,height=900)
cover.maxsize(width=1000,height=1300)

hospital=Label(cover,text="HOPE HOSPITAL",font=(UNDERLINE,19))
hospital.pack()
photo1=Image.open("cover.png")
resize_photo1=photo1.resize((200,200))
final_image1=ImageTk.PhotoImage(resize_photo1)
medical_team=Label(cover,image=final_image1,width=0,height=300)
medical_team.place(x=0,y=20)

# def login_page():
#     window = Tk()
#     window.title("Simon Hospital")
#     window.configure(bg='sky blue') # background color 
#     window.minsize(width=1200,height=500)
def Login_page_2():
    window = Tk()
    window.configure(bg='sky blue') # background color
    l2 = Label(window,text="Medical Team",bg = 'black',fg='white',font=20)
    l2.place(x = 10,y=20)
    l3 = Label(window,text='USER NAME :-',bg='green',fg='white')
    l3.place(x=10,y=60)
    e1 = Entry(window,width=20,font=("Calibri",10))
    e1.place(x =100,y=59)
    l4 = Label(window,text='PASSWORD :-',bg= 'green',fg ='white')
    l4.place(x =10,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10))
    e2.place(x =100,y=100)
    btn = Button(window,text='LOGIN',bg='red')
    btn.place(x=95,y=140)
    
def reg_p():
    window = Tk()
    l=Label(window,text="Fill all the details",font = 100)
    l.place(x= 250)
    l1 = Label(window,text="First Name",font=50)
    l1.place(x=0,y=50)
    e1= Entry(window,width=20,font=("Calibri",10))
    e1.place(x=100,y=54)
    l2 = Label(window,text="Last Name",font = 50)
    l2.place(x=0,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10))
    e2.place(x =100,y=105)
    
def login_page():
    window = Tk()
    window.configure(bg='sky blue') # background color
    l2 = Label(window,text="For Patient",bg = 'black',fg='white',font=20)
    l2.place(x = 10,y=20)
    l3 = Label(window,text='USER NAME :-',bg='green',fg='white')
    l3.place(x=10,y=60)
    e1 = Entry(window,width=20,font=("Calibri",10))
    e1.place(x =100,y=59)
    l4 = Label(window,text='PASSWORD :-',bg= 'green',fg ='white')
    l4.place(x =10,y=100)
    e2 = Entry(window,width=20,font=("Calibri",10))
    e2.place(x =100,y=100)
    btn = Button(window,text='LOGIN',bg='red')
    btn.place(x=95,y=140)
    btn1 = Button(window,text="Create New account",bg='Green',command = reg_p)
    btn1.place(x=95,y=180)
    
staff=Button(cover,text="For medical team",font=800,command=Login_page_2)
staff.place(x=20,y=280)



photo2=Image.open("cover2.png")
resize_photo2=photo2.resize((200,200))
final_image2=ImageTk.PhotoImage(resize_photo2)
patient_team=Label(cover,image=final_image2,width=0,height=300)
patient_team.place(x=500,y=20)

patient=Button(cover,text="For patient",font=800,command=login_page)
patient.place(x=550,y=280)


if __name__ == "__main__":
    mainloop()