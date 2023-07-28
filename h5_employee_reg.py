from tkinter import*
import tkinter 
from PIL import ImageTk
import pymysql
from tkinter import ttk
from datetime import date


def EMP():
    global emp_address, emp_contact, emp_age, emp_CT, emp_date, emp_email, emp_ID, emp_name, emp_gender, emp_exp, emp_dept,d
    global rootE,regform,id,name,gender,email,ct,addr,c1,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    
    class Table:
        def __init__(self,rootE):
            self.rootE=rootE
            
            
            frame1=Frame(self.rootE, bg='#022B63', borderwidth=1)
            frame1.place(relx=0.5, relheight=1, relwidth=0.5)
            scroll_x=Scrollbar(frame1, orient=HORIZONTAL)
            scroll_y=Scrollbar(frame1, orient=VERTICAL)
            self.emp_table=ttk.Treeview(frame1, columns=("emp_id", "name", "gender", "age","doj","Phno","address","email","salary","department","exper"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.emp_table.xview)
            scroll_y.config(command=self.emp_table.yview)
            self.emp_table.heading("emp_id",text="EMPLOYEE ID")
            self.emp_table.heading("name",text="Name")
            self.emp_table.heading("gender",text="Gender")
            self.emp_table.heading("age",text="Age")
            self.emp_table.heading("doj",text="Date_of_Joining")
            self.emp_table.heading("Phno",text="Contact Number")
            self.emp_table.heading("address",text="Address")
            self.emp_table.heading("email",text="Email-ID")
            self.emp_table.heading("salary",text="Salary(in Rs.)")
            self.emp_table.heading("department",text="Department")
            self.emp_table.heading("exper",text="Experience")
            self.emp_table['show']='headings'
            self.emp_table.pack()
            conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
            c=conn.cursor()
            c.execute("select* from employee")
            rows=c.fetchall()
            if len(rows)!=0:
                self.emp_table.delete(*self.emp_table.get_children())

                for row in rows:
                    self.emp_table.insert("",END,values=row)
                print("Connected to employee table of vtreat database")
                conn.commit()
                conn.close()
                
            else:
                print("Not done")



    rootE=Tk()
    call=Table(rootE)
    rootE.title("EMPLOYEE REGISTRATION FORM")
    menubar=tkinter.Menu(rootE)
    filemenu=tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New",command=EMP)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=EXO)

    emenu=tkinter.Menu(menubar, tearoff=0)
    emenu.add_command(label="Update",command=E_UPDATE)
    emenu.add_separator()
    emenu.add_command(label="Search", command=E_Display)
    emenu.add_separator()
    emenu.add_command(label="Delete", command=D_display)

    helpmenu=tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help",command=hp)
    helpmenu.add_command(label="About",command=ab)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=emenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootE.config(menu=menubar)

    frame2=Frame(rootE, bg='#022B63')
    frame2.place(x=0, y=0, relheight=1, relwidth=0.5)

    regform=tkinter.Label(frame2,text="EMPLOYEE REGISTRATION FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")

    id=tkinter.Label(frame2,text="EMPLOYEE ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_ID=tkinter.Entry(frame2,width=50)

    name=tkinter.Label(frame2,text="NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_name = tkinter.Entry(frame2,width=50)

    gender=tkinter.Label(frame2,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_gender=tkinter.Listbox(frame2,selectmode='SINGLE', exportselection=0, height=2, width=50)
    emp_gender.insert(tkinter.END, "M")
    emp_gender.insert(tkinter.END, "F")

    age=tkinter.Label(frame2, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_age=tkinter.Entry(frame2,width=50)

    datel=tkinter.Label(frame2, text="DATE OF JOINING",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    d=date.today()
    emp_date=tkinter.Entry(frame2,width=50)
    emp_date.insert(0,d)
    

    c1=tkinter.Label(frame2, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_contact=tkinter.Entry(frame2,width=50)

    addr=tkinter.Label(frame2, text="ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_address=tkinter.Entry(frame2,width=50)

    email=tkinter.Label(frame2, text="EMAIL",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_email = tkinter.Entry(frame2,width=50)

    ct=tkinter.Label(frame2,text="SALARY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_CT=tkinter.Entry(frame2,width=50)            

    dept=tkinter.Label(frame2,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_dept = tkinter.Listbox(frame2, selectmode='SINGLE', exportselection=0, height=5, width=50)
    emp_dept.insert(tkinter.END, "Doctor")
    emp_dept.insert(tkinter.END, "Nurse")
    emp_dept.insert(tkinter.END, "Compounder")
    emp_dept.insert(tkinter.END, "Housekeeping")
    emp_dept.insert(tkinter.END, "Receptionist")

    exp=tkinter.Label(frame2,text="EXPERIENCE(in years)",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    emp_exp=tkinter.Entry(frame2, width=50)
 

    back=tkinter.Button(frame2,text="BACK",command=rootE.destroy,font=("Arial",12,"bold"), fg="white", bg="#022B63")    #,bd=0)
    SUBMIT=tkinter.Button(frame2,text="SUBMIT",command=IN_emp,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)

    
    regform.grid(row=0, column=0,columnspan=3)
    id.grid(row = 1, column = 0, pady=5,sticky=W)
    emp_ID.grid(row = 1, column = 1, pady=5)
    name.grid(row = 2, column = 0, pady=5,sticky=W)
    emp_name.grid(row = 2, column = 1, pady=5)
    gender.grid(row = 3, column = 0, pady=5,sticky=W)
    emp_gender.grid(row = 3, column = 1, pady=5)
    age.grid(row = 4, column = 0, pady=5,sticky=W)
    emp_age.grid(row = 4, column = 1, pady=5)
    datel.grid(row = 5, column = 0, pady=5,sticky=W)
    emp_date.grid(row = 5, column = 1, sticky=W)
    c1.grid(row = 6, column = 0, pady=5,sticky=W)
    emp_contact.grid(row = 6, column = 1, pady=5)
    addr.grid(row = 7, column = 0, pady=5,sticky=W)
    emp_address.grid(row = 7, column = 1, pady=5)
    email.grid(row = 8, column = 0, pady=5,sticky=W)
    emp_email.grid(row = 8, column = 1, pady=5)
    ct.grid(row = 9, column = 0, pady=5, sticky=W)
    emp_CT.grid(row = 9, column = 1, pady=5)
    dept.grid(row = 10, column = 0, pady=5,sticky=W)
    emp_dept.grid(row = 10, column = 1, pady=5)
    exp.grid(row = 11, column = 0, pady=5,sticky=W)
    emp_exp.grid(row = 11, column = 1, pady=5)

    SUBMIT.grid(row = 13, column = 0)
    back.grid(row = 13, column = 1)

    rootE.iconbitmap('logo.ico')
    rootE.title("V tReat_emp_form")
    rootE.geometry("1199x600+100+50")


    rootE.mainloop()

#variables

rootE=None
emp_ID=None
emp_name=None
emp_dob=None
emp_address=None
emp_gender=None
emp_BG=None
emp_email=None
emp_contact=None
emp_contactalt=None
emp_CT=None
p=None

#input EMPLOYEE form
def IN_emp():
    global ee1, ee2, ee3, ee4, ee5, ee6, ee7, ee8, ee9, ee10, ee11, ce1,conn,d
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    ee1=emp_ID.get()
    ee2=emp_name.get()
    ee3=emp_gender.get(tkinter.ACTIVE)
    ee4=emp_age.get()
    ee5=d
    ee6=emp_contact.get()
    ee7=emp_address.get()
    ee8=emp_email.get()
    ee9=emp_CT.get()
    ee10=emp_dept.get(tkinter.ACTIVE)
    ee11=emp_exp.get()

    c.execute('INSERT INTO EMPLOYEE(name,gender,age,date_of_joining, contact,address,email,salary,department,experience) VALUES("{}","{}",{},"{}",{},"{}","{}","{}","{}",{})'.format(ee2,ee3,ee4,ee5,ee6,ee7,ee8,ee9,ee10,ee11))
    rootE.destroy()
    tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM","EMPLOYEE REGISTERED IN DATABASE")
    conn.commit()
    conn.close()
    
    



#exit from employee form
def EXO():
    rootE.destroy()

#function for employee form help
def hp():
    tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM","For any help regarding the software \n CONTACT the creators using the details given in the About Section")

def ab():
   tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM"," The software is designed and created by \n \n Vihaan S. Kumar Contact-456789xxxx\n Rohan Nag Contact-789659xxxx \n \n Email- pydeveloper@gmail.com \n \n©2020")




'''=====================================================================EMPDELSU_CODE====================================================================='''


#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10, dis11
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    frameS.place_forget() #forget hides the frame
    if searchL.get(tkinter.ACTIVE)=="ID":
        inp_s=int(entry.get())
        c.execute('select * from employee where id=%d;'%inp_s)
        t=c.fetchall()
    elif searchL.get(tkinter.ACTIVE)=="Name":
        inp_s=str(entry.get())
        c.execute('select * from employee where name="{}";'.format(inp_s))
        t=c.fetchall()
    if (len(t)==0):
        messagebox.showerror("Error","NO employee WITH SUCH ID;", parent=rootS)
    else:

        for i in t:
            emp_det=tkinter.Label(rootS,text="EMPLOYEE DETAILS",font="Arial 24 bold",fg="light gray", bg="#022B63")
            l1=tkinter.Label(rootS,text="EMPLOYEE ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="EMPLOYEE NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="EMPLOYEE GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="EMPLOYEE AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="DATE OF JOINING",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="EMPLOYEE CONTACT_NO",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis6=tkinter.Label(rootS,text=i[5])
            l7=tkinter.Label(rootS,text="EMPLOYEE ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis7=tkinter.Label(rootS,text=i[6])
            l8=tkinter.Label(rootS,text="EMPLOYEE EMAIL-ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis8=tkinter.Label(rootS,text=i[7])
            l9=tkinter.Label(rootS,text="SALARY ",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis9=tkinter.Label(rootS,text=i[8])
            l10=tkinter.Label(rootS,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis10=tkinter.Label(rootS,text=i[9])
            l11=tkinter.Label(rootS,text="EXPERIENCE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis11=tkinter.Label(rootS,text=i[10])

            emp_det.grid(row=0, column=0, pady=5, padx=2,columnspan=2)
            l1.grid(row=1, column=0, pady=5, padx=2)
            dis1.grid(row=1, column=1, pady=5, padx=2)
            l2.grid(row=2, column=0, pady=5, padx=2)
            dis2.grid(row=2, column=1, pady=5, padx=2)
            l3.grid(row=3, column=0, pady=5, padx=2)
            dis3.grid(row=3, column=1, pady=5, padx=2)
            l4.grid(row=4, column=0, pady=5, padx=2)
            dis4.grid(row=4, column=1, pady=5, padx=2)
            l5.grid(row=5, column=0, pady=5, padx=2)
            dis5.grid(row=5, column=1, pady=5, padx=2)
            l6.grid(row=6, column=0, pady=5, padx=2)
            dis6.grid(row=6, column=1, pady=5, padx=2)
            l7.grid(row=7, column=0, pady=5, padx=2)
            dis7.grid(row=7, column=1, pady=5, padx=2)
            l8.grid(row=8, column=0, pady=5, padx=2)
            dis8.grid(row=8, column=1, pady=5, padx=2)
            l9.grid(row=9, column=0, pady=5, padx=2)
            dis9.grid(row=9, column=1, pady=5, padx=2)
            l10.grid(row=10, column=0, pady=5, padx=2)
            dis10.grid(row=10, column=1, pady=5, padx=2)
            l11.grid(row=11, column=0, pady=5, padx=2)
            dis11.grid(row=11, column=1, pady=5, padx=2)
            conn.commit()


def eXO():
    rootS.destroy()

##search window
def E_Display():
    global rootS,head,inp_s,entry,searchB, frameS, searchL
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    frameS=tkinter.Frame(rootS)
    
    head=tkinter.Label(frameS,text="Search Using:",fg="red")
    searchL=tkinter.Listbox(frameS, selectmode='SINGLE', exportselection=0, height=2, width=20)
    searchL.insert(tkinter.END,"Name")
    searchL.insert(tkinter.END,"ID")

    entry=tkinter.Entry(frameS)
    searchB=tkinter.Button(frameS,text='SEARCH',command=Search_button)
    
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=E_Display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    
    
    head.grid(row=0,column=0, columnspan=2)
    searchL.grid(row=1,column=0,columnspan=2)
    entry.grid(row=2,column=0,columnspan=2)
    searchB.grid(row=3,column=0, columnspan=2)
    frameS.place(x=0,y=0)
    rootS.iconbitmap('logo.ico')
    rootS.mainloop()


#DELETE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    inp_d = int(entry1.get())
    c.execute("select * from EMPLOYEE where id=%d;"%inp_d)
    p=c.fetchall()
    if (len(p)==0):
        errorD = tkinter.Label(rootD, text="EMPLOYEE RECORD NOT FOUND")
        errorD.pack()
    else:
        c.execute('DELETE FROM EMPLOYEE where id=%d;'%inp_d)
        tkinter.messagebox.showinfo("VtReat Database System", "The EMPLOYEE record has been permanently deleted")
        conn.commit()
        rootD.destroy()
        rootE.destroy()
        


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="ENTER EMPLOYEE ID TO DELETE",fg="blue")
    entry1=tkinter.Entry(rootD)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button)
    headD.pack()
    entry1.pack()
    DeleteB.pack()
    rootD.iconbitmap('logo.ico')
    rootD.mainloop()




##-----EMPLOYEE UPDATE SCREEN -----##
def E_UPDATE():
    global empu_ID,empu_name, empu_gender, empu_age,empu_date,empu_contact,empu_address,empu_email,empu_CT, n,empu_dept,empu_exp
    global rootU, regform, id, name, dob, gender, email, ct, addr, c1, UPDATE, menubar, filemenu
    rootU = tkinter.Tk()
    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Help", command=hp)
    filemenu.add_command(label="About", command=ab)
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
     
    def Pupdate_box():
        global empu_ID,empu_name, empu_gender, empu_age,empu_date,empu_contact,empu_address,empu_email,empu_CT, n,empu_dept,empu_exp
        conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
        c=conn.cursor()
        n=int(empu_ID.get())
        c.execute('Select * from employee where id=%d'%n)
        p=c.fetchall()
        if ((len(p))!=0):
            name=tkinter.Label(rootU,text="EMPLOYEE NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_name = tkinter.Entry(rootU,width=50)
            gender=tkinter.Label(rootU,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_gender=tkinter.Listbox(rootU,selectmode='SINGLE', exportselection=0, height=1, width=50)
            empu_gender.insert(tkinter.END, "M")
            empu_gender.insert(tkinter.END, "F")

            age=tkinter.Label(rootU, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_age=tkinter.Entry(rootU,width=50)

            date=tkinter.Label(rootU, text="DATE OF JOINING",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_date=tkinter.Entry(rootU,width=50)
            
            c1=tkinter.Label(rootU, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_contact=tkinter.Entry(rootU,width=50)

            addr=tkinter.Label(rootU, text="ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_address=tkinter.Entry(rootU,width=50)

            email=tkinter.Label(rootU, text="EMAIL",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_email = tkinter.Entry(rootU,width=50)

            ct=tkinter.Label(rootU,text="SALARY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_CT=tkinter.Entry(rootU,width=50)

            dept=tkinter.Label(rootU,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_dept = tkinter.Listbox(rootU, selectmode='SINGLE', exportselection=0, height=5, width=50)
            empu_dept.insert(tkinter.END, "Doctor")
            empu_dept.insert(tkinter.END, "Nurse")
            empu_dept.insert(tkinter.END, "Compounder")
            empu_dept.insert(tkinter.END, "Housekeeping")
            empu_dept.insert(tkinter.END, "Receptionist")

            exp=tkinter.Label(rootU,text="EXPERIENCE(in years)",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            empu_exp=tkinter.Entry(rootU, width=50)      

            c.execute('Select * from EMPLOYEE where id={};'.format(empu_ID.get()))
            t=c.fetchall()
            for i in t:
                empu_name.insert(0,i[1])
                empu_gender.insert(0,i[2])
                empu_age.insert(0,i[3])
                empu_date.insert(0,i[4])
                empu_contact.insert(0,i[5])
                empu_address.insert(0,i[6])
                empu_email.insert(0,i[7])
                empu_CT.insert(0,i[8])
                empu_exp.insert(0,i[10])


            UPDATE=tkinter.Button(rootU,text="UPDATE",command=up1,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)
            
            name.grid(row = 2, column = 0, pady=5,sticky=W)
            empu_name.grid(row = 2, column = 1, pady=5)
            gender.grid(row = 3, column = 0, pady=5,sticky=W)
            empu_gender.grid(row = 3, column = 1, pady=5)
            age.grid(row = 4, column = 0, pady=5,sticky=W)
            empu_age.grid(row = 4, column = 1, pady=5)
            date.grid(row = 5, column = 0, pady=5,sticky=W)

            empu_date.grid(row = 5, column = 1, pady=5)
            c1.grid(row = 6, column = 0, pady=5,sticky=W)
            empu_contact.grid(row = 6, column = 1, pady=5)
            addr.grid(row = 7, column = 0, pady=5,sticky=W)
            empu_address.grid(row = 7, column = 1, pady=5)
            email.grid(row = 8, column = 0, pady=5,sticky=W)
            empu_email.grid(row = 8, column = 1, pady=5)
            ct.grid(row = 9, column = 0, pady=5, padx=2, sticky=W)
            empu_CT.grid(row = 9, column = 1, pady=5)
            dept.grid(row = 10, column = 0, pady=5,sticky=W)
            empu_dept.grid(row = 10, column = 1, pady=5)
            exp.grid(row = 11, column = 0, pady=5,sticky=W)
            empu_exp.grid(row = 11, column = 1, pady=5)
            UPDATE.grid(row = 13, column = 0, columnspan=2)
        else:
            tkinter.messagebox.showerror("V tReat DATABSE SYSTEM", "EMPLOYEE IS NOT REGISTERED")

    upform=tkinter.Label(rootU,text="UPDATE FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")
    id=tkinter.Label(rootU,text="ID OF EMPLOYEE TO UPDATE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    empu_ID=tkinter.Entry(rootU,width=50)
    id_bt=tkinter.Button(rootU, text="Search",command=Pupdate_box,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=23)



    
    upform.grid(row=0, column=0,columnspan=3)
    id.grid(row = 1, column = 0, pady=5,sticky=W)
    empu_ID.grid(row = 1, column = 1, pady=5)
    id_bt.grid(row = 1, column = 2, pady=5)
    rootU.iconbitmap('logo.ico')
    rootU.mainloop()

#Update command of button
def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    u1=empu_ID.get()
    u2=empu_name.get()
    u3=empu_gender.get(tkinter.ACTIVE)
    u4=empu_age.get()
    u5=empu_date.get()
    u6=empu_contact.get()
    u7=empu_address.get()
    u8=empu_email.get()
    u9=empu_CT.get()
    u10=empu_dept.get(tkinter.ACTIVE)
    u11=empu_exp.get()


    
    c.execute('UPDATE EMPLOYEE SET name="{}",gender="{}",age={},date_of_joining="{}", contact={},address="{}",email="{}",salary={},department="{}",experience={} where id={};'.format( u2, u3, u4, u5, u6,u7,u8,u9,u10,u11,u1))
  
    tkinter.messagebox.showinfo("V tReat DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
    conn.commit()
    rootU.destroy()


def EXITT():
    rootU.destroy()

