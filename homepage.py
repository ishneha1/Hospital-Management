from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.minsize(height=900,width=700)
root.maxsize(height=900,width=700)

background=Image.open("homepage1.png")
back_ground1=background.resize((1000,700))
background1=ImageTk.PhotoImage(back_ground1)
back_ground=Label(root,image=background1)
back_ground.place(x=0,y=0)




mainloop()