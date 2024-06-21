from tkinter import * 
front_end=Tk()
front_end.title("login")
front_end.minsize(width=600,height=800)
front_end.maxsize(width=600,height=800)

bg=PhotoImage(file="o2.png")
photo1=Label(front_end,image=bg).place(x=100,y=150)




welcome=Label(front_end,text="HOSPITAL MANAGEMENT SYSTEM").place(x=200,y=10)
staff=Label(front_end,text="FOR STAFF").place(x=0,y=50)
patient=Label(front_end,text="FOR PATIENT").place(x=300,y=50)
staff_id=Label(front_end,text="Staff I.D").place(x=0,y=70)
patient_id=Label(front_end,text="Patient I.D").place(x=300,y=70)
password_s=Label(front_end,text="Password").place(x=0,y=90)
password_p=Label(front_end,text="Password").place(x=300,y=90)
es1=Entry().place(x=70,y=70)
es2=Entry().place(x=70,y=90)
ep1=Entry().place(x=370,y=70)
ep2=Entry().place(x=370,y=90)

logins=Button(text="login").place(x=0,y=120)
loginp=Button(text="login").place(x=300,y=120)
ts=Label(front_end,text="Not registered?Join Now!").place(x=60,y=120)
tp=Label(front_end,text="Not registered?Join Now!").place(x=360,y=120)

mainloop()
