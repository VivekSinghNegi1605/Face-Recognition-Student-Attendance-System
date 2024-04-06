from tkinter import *
from PIL import Image,ImageTk


class Developer :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Student Attendance System")

        img=Image.open(r"image\developer_bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=840,y=60,width=500,height=620)

        dev_label=Label(main_frame,text="Hello my name is Vivek Singh Negi",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=10)

        dev_label=Label(main_frame,text="I belong to Pithoragarh, Uttarakhand, India",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Currently I am pursuing Computer Science Engineering ",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=70)

        dev_label=Label(main_frame,text="from Graphic Era Hill University, Dehradun",font=("times new roman",14,"bold"),bg="white")
        dev_label.place(x=0,y=90)




if __name__=="__main__" :
    root=Tk()
    obj=Developer(root)
    root.mainloop()