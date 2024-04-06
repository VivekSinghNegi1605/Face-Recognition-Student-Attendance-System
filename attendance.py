from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector


class Attendance :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Student Attendance System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img=Image.open(r"image\bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="ATTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=100,y=80,width=1100,height=620)


        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=80,y=10,width=950,height=600)

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=20,y=80,width=900,height=490)

        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_x.config(command=self.AttendanceReportTable.xview)
        scrol_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetchData()


    def fetchData(self) :
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendance")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data :
                self.AttendanceReportTable.insert("",END,values=i)

            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])






if __name__=="__main__" :
    root=Tk()
    obj=Attendance(root)
    root.mainloop()