from tkinter import*
from h2_main_menu import menu
from PIL import ImageTk
from tkinter import messagebox


            
class Login:
    def __init__(self,root):
        self.root=root
        #BGimage
        self.bg=ImageTk.PhotoImage(file="hospital.jpg")
        self.bg_image=Label(root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Frame
        frame=Frame(self.root, bg='white').place(x=80, y=200, height=320, width=500)
        title=Label(frame, text="Welcome to", font=("Arial Rounded MT Bold",12,"bold"), fg="#128fcc", bg="white").place(x=260,y=200)
        title=Label(frame, text="V tReat", font=("Arial Rounded MT Bold",35,"bold"), fg="#128fcc", bg="white").place(x=220,y=220)

        lbl_user=Label(frame, text="Username", font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=100,y=300)
        self.txt_user=Entry(frame, font=("Times new roman",15),bg="lighTgray", text="Here")
        self.txt_user.place(x=100,y=325, relwidth=0.38,height=35)
            
        lbl_pass=Label(frame, text="Password", font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=100,y=370)
        self.txt_pass=Entry(frame, font=("Times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=100,y=395,relwidth=0.38,height=35)

        lbl=Label(frame, text="We care for you!!", bg="white", bd=0, font=("Times new roman", 15), fg="#128fcc").place(x=100,y=440)
        login_bt=Button(frame, text="Login", bg="#128fcc", bd=0, font=("Times new roman", 18, "bold"),command=self.loginfunc, fg="white").place(x=260,y=510, width=100)

    def loginfunc(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.txt_pass.get()!="admin" or self.txt_user.get()!="admin":
            messagebox.showerror("Error","Invalid username/password", parent=self.root)
        else:
            root.destroy()
            menu()
            
        
root=Tk()
root.iconbitmap('logo.ico')
root.title("V tReat_LOGIN")
root.geometry("1199x600+100+50")
Call=Login(root)

root.resizable(False,False)
root.mainloop()
