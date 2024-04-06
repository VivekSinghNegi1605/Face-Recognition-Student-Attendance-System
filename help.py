from tkinter import *
from PIL import Image,ImageTk


class Help :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Student Attendance System")

        img=Image.open(r"image\helpdesk_bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=45)


        dev_label=Label(bg_img,text="First Contact No - 6399245057",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=450,y=350,width=500,height=45)

        dev_label=Label(bg_img,text="Second Contact No - 7078704346",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=450,y=400,width=500,height=45)

        dev_label=Label(bg_img,text="Email - viveksinghnegi1605@gmail.com",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=450,y=450,width=500,height=45)




if __name__=="__main__" :
    root=Tk()
    obj=Help(root)
    root.mainloop()