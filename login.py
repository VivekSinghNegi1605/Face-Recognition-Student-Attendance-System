from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_Student_Attendance_System


def main() :
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        img=Image.open(r"image\bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        frame=Frame(bg_img,bd=2,bg="antique white")
        frame.place(x=520,y=160,width=340,height=450)

        img1=Image.open(r"image\login_logo.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=165,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="antique white")
        get_str.place(x=96,y=100)

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="antique white")
        username.place(x=50,y=160)

        self.txtuser=ttk.Entry(frame,width=30,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=186)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="antique white")
        password.place(x=50,y=230)

        self.txtpass=ttk.Entry(frame,show="*",width=30,font=("times new roman",15,"bold"))
        self.txtpass.place(x=20,y=256)

        img2=Image.open(r"image\login_logo.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(frame,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=20,y=160)

        img3=Image.open(r"image\password.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(frame,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=20,y=230)

        loginbtn=Button(frame,text="Login",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),fg="ghost white",bg="red",activeforeground="black",activebackground="dark red")
        loginbtn.place(x=120,y=300,width=100)

        forgetbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="antique white",activebackground="antique white")
        forgetbtn.place(x=20,y=370)

        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="antique white",activebackground="antique white")
        forgetbtn.place(x=20,y=400)

    def register_window(self) :
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "Vivek" and self.txtpass.get() == "Vivek@123":
            messagebox.showinfo("success", "Welcome to Face Recognition Student Attendance System")
            self.new_window=Toplevel(self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Student_Attendance_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Plese your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter your new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid security answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                messagebox.showinfo("Info","your password has been reset , please login new password",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="white", fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select","Your Birth place","Your Dad's Name","Your Mom's name","Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        img=Image.open(r"image\bg.jpg")
        img=img.resize((1366,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)


        frame=Frame(bg_img,bd=2,bg="azure")
        frame.place(x=250,y=100,width=900,height=550)

        Register_frame=LabelFrame(frame,bd=2,bg="azure",relief=RIDGE,text="REGISTER HERE",font=("times new roman",20,"bold"), fg="dark green")
        Register_frame.place(x=100,y=40,width=650,height=400)

        fname=Label(Register_frame,text="First and Middle Name",font=("times new roman",15,"bold"),bg="azure")
        fname.grid(row=1,column=1,padx=20,pady=5,sticky=W)

        fname_entry=ttk.Entry(Register_frame,textvariable=self.var_fname,width=30,font=("times new roman",13,"bold"))
        fname_entry.grid(row=2,column=1,padx=20,pady=5,sticky=W)

        lname=Label(Register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="azure")
        lname.grid(row=1,column=2,padx=20,pady=5,sticky=W)

        lname_entry=ttk.Entry(Register_frame,textvariable=self.var_lname,width=30,font=("times new roman",13,"bold"))
        lname_entry.grid(row=2,column=2,padx=20,pady=5,sticky=W)

        contact=Label(Register_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="azure")
        contact.grid(row=3,column=1,padx=20,pady=5,sticky=W)

        contact_entry=ttk.Entry(Register_frame,textvariable=self.var_contact,width=30,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=20,pady=5,sticky=W)

        email=Label(Register_frame,text="Email or Username",font=("times new roman",15,"bold"),bg="azure")
        email.grid(row=3,column=2,padx=20,pady=5,sticky=W)

        email_entry=ttk.Entry(Register_frame,textvariable=self.var_email,width=30,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=2,padx=20,pady=5,sticky=W)

        security_Q=Label(Register_frame,text="Security Question",font=("times new roman",15,"bold"),bg="azure")
        security_Q.grid(row=6,column=1,padx=20,pady=5,sticky=W)

        Security_combo=ttk.Combobox(Register_frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly",width=28)
        Security_combo["values"]=("Select","Your Birth place","Your Dad's Name","Your Mom's name","Your Pet Name")
        Security_combo.current(0)
        Security_combo.grid(row=7,column=1,padx=20,pady=5,sticky=W)

        security_A=Label(Register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="azure")
        security_A.grid(row=6,column=2,padx=20,pady=5,sticky=W)

        security_entry=ttk.Entry(Register_frame,textvariable=self.var_securityA,width=30,font=("times new roman",13,"bold"))
        security_entry.grid(row=7,column=2,padx=20,pady=5,sticky=W)

        pswd=Label(Register_frame,text="Password",font=("times new roman",15,"bold"),bg="azure")
        pswd.grid(row=8,column=1,padx=20,pady=5,sticky=W)

        pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_pass,width=30,font=("times new roman",13,"bold"))
        pswd_entry.grid(row=9,column=1,padx=20,pady=5,sticky=W)

        confirm_pswd=Label(Register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="azure")
        confirm_pswd.grid(row=8,column=2,padx=20,pady=5,sticky=W)

        confirm_pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_confpass,width=30,font=("times new roman",13,"bold"))
        confirm_pswd_entry.grid(row=9,column=2,padx=20,pady=5,sticky=W)

        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree with terms and conditions", font=("times new roman", 12, "bold"), bg="azure", onvalue=1, offvalue=0)
        checkbtn.place(x=120, y=390)

        b1=Button(frame,text="Register",command=self.register_data,cursor="hand2",font=("times new roman",15,"bold"),fg="ghost white",bg="red",activeforeground="black",activebackground="dark red")
        b1.place(x=100, y=460, width=200)

        b2=Button(frame,text="Cancle",command=self.return_login,cursor="hand2",font=("times new roman",15,"bold"),fg="ghost white",bg="red",activeforeground="black",activebackground="dark red")
        b2.place(x=430, y=460, width=200)


    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            messagebox.showerror("Error",'Invalid email Enter valid email like anc123@gmail.com ',parent=self.root)

        elif not ("@" or "!" or "$" or "-" or "." or "#" ) in self.var_pass.get():
            messagebox.showerror("Error",'Invalid password Please Enter Strong password like Abc@123 ',parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "user already exists, plaese try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo("Success","Register Successfully",parent=self.root)
            conn.commit()
            conn.close()
            self.root.destroy()

    def return_login(self):
        self.root.destroy()



if __name__ == "__main__":
    main()
