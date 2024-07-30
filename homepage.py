from tkinter import *
from PIL import ImageTk,Image
root= Tk()
root.title("Hope Hospital")
root.iconbitmap('icon.ico')
root.minsize(height=900,width=700)
root.maxsize(height=900,width=700)


#for importing info
def info():
    root.destroy()
    import about_us


#for information icon
info=Label(root,text="About us",font=("Helvetica", 20))
info.place(x=0,y=120)
info_pic=Image.open("home.ico")
resize_info_pic=info_pic.resize((40,60))
final_info_image=ImageTk.PhotoImage(resize_info_pic)
info_icon=Button(root, image=final_info_image, width=0, height=0,command=info)
info_icon.place(x=35,y=50)

#import dashboard
def doc():
    root.destroy()
    import dashboard

#for doctors
doctor=Label(root,text="Our Doctors",font=("Helvetica", 20))
doctor.place(x=250,y=120)
doctor_pic=Image.open("doc.ico")
resize_doc_pic=doctor_pic.resize((40,60))
final_doc_image=ImageTk.PhotoImage(resize_doc_pic)
doc_icon=Button(root,image=final_doc_image,width=0,height=0,command=doc)
doc_icon.place(x=300,y=50)



mainloop()