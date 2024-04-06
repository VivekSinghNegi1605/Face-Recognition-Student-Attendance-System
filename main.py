import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
import os
from time import strftime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_Student_Attendance_System :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Student Attendance System")

        img=Image.open(r"image\bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="FACE RECOGNITION STUDENT ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        def time() :
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        img2=Image.open(r"image\student.jpg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=130,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=350,width=220,height=40)

        img3=Image.open(r"image\face.jpg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(bg_img,image=self.photoimg3,command=self.face_data,cursor="hand2")
        b2.place(x=450,y=130,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_1.place(x=450,y=350,width=220,height=40)

        img4=Image.open(r"image\attendance.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b3.place(x=700,y=130,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b3_1.place(x=700,y=350,width=220,height=40)

        img5=Image.open(r"image\help.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.help_data)
        b4.place(x=950,y=130,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b4_1.place(x=950,y=350,width=220,height=40)

        img6=Image.open(r"image\train.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=420,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b5_1.place(x=200,y=640,width=220,height=40)

        img7=Image.open(r"image\photo.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b6=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b6.place(x=450,y=420,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b6_1.place(x=450,y=640,width=220,height=40)

        img8=Image.open(r"image\developer.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b7=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.developer_data)
        b7.place(x=700,y=420,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b7_1.place(x=700,y=640,width=220,height=40)

        img9=Image.open(r"image\exit.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b8=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b8.place(x=950,y=420,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b8_1.place(x=950,y=640,width=220,height=40)


    def open_img(self) :
        os.startfile(r"data")


    def iExit(self) :
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit from this project",parent=self.root)
        if self.iExit>0 :
            self.root.destroy()
        else :
            return
        

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self) :
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self) :
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_data(self) :
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self) :
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def help_data(self) :
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




if __name__=="__main__" :
    root=Tk()
    obj=Face_Recognition_Student_Attendance_System(root)
    root.mainloop()