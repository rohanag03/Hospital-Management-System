from tkinter import*
import tkinter 
from PIL import ImageTk
import pymysql
from tkinter import ttk
from datetime import datetime
from datetime import date



def APP():
    global app_name, app_age,app_gender,app_contact,app_qn,app_date,app_time,d_sel, app_dept, fee_var
    global roota,regform,id,name,gender,email,ct,addr,c1,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    
    class Table:
        def __init__(self,roota):
            self.roota=roota
            
            
            frame2=Frame(self.roota, bg='#022B63', borderwidth=1)
            frame2.place(rely=0.5, relheight=0.5, relwidth=1)
            scroll_x=Scrollbar(frame2, orient=HORIZONTAL)
            scroll_y=Scrollbar(frame2, orient=VERTICAL)
            self.app_table=ttk.Treeview(frame2, columns=("id", "name", "gender", "age","Phno","Q_no","time","date","doctor","department","c_fee"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.app_table.xview)
            scroll_y.config(command=self.app_table.yview)
            self.app_table.heading("id",text="Patient ID")
            self.app_table.heading("name",text="Name")
            self.app_table.heading("gender",text="Gender")
            self.app_table.heading("age",text="Age")
            self.app_table.heading("Phno",text="Contact Number")
            self.app_table.heading("Q_no",text="Queue No.")
            self.app_table.heading("time",text="Appointment Date")
            self.app_table.heading("date",text="Appointment Time")
            self.app_table.heading("doctor",text="Consulting Doctor")
            self.app_table.heading("department",text="Department")
            self.app_table.heading("c_fee",text="Consultation Fee")
            
            self.app_table['show']='headings'
            self.app_table.pack()
            conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
            c=conn.cursor()
            c.execute("select* from appointments")
            rows=c.fetchall()
            if len(rows)!=0:
                self.app_table.delete(*self.app_table.get_children())
                for row in rows:
                    self.app_table.insert("",END,values=row)
                print("Connected with appointments table of vtreat database")
                conn.commit()
                conn.close()
                
            else:
                print("Failed to connect with appointments table of vtreat database")



    roota=Tk()
    call=Table(roota)
    roota.title("APPOINTMENT BOOKING")
    menubar=tkinter.Menu(roota)
    filemenu=tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New",command=APP)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=EXO)

    emenu=tkinter.Menu(menubar, tearoff=0)
    emenu.add_command(label="Update",command=A_UPDATE)
    emenu.add_separator()
    emenu.add_command(label="Search", command=A_Display)
    emenu.add_separator()
    emenu.add_command(label="Delete", command=D_display)

    helpmenu=tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help",command=hp)
    helpmenu.add_command(label="About",command=ab)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=emenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    roota.config(menu=menubar)

    frame1=Frame(roota, bg='#022B63')
    frame1.place(x=0, y=0, relheight=0.5, relwidth=1)

    regform=tkinter.Label(frame1,text="APPPOINTMENTS BOOKING FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")


    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    c.execute("select max(queue_no) from APPOINTMENTS;")
    i=c.fetchone()
    i=i[0]+1

    qn=tkinter.Label(frame1, text="QUEUE NO.",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_qn=tkinter.Entry(frame1,width=10)
    app_qn.insert(tkinter.END, i)
        
    name=tkinter.Label(frame1,text="NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_name = tkinter.Entry(frame1,width=25)

    gender=tkinter.Label(frame1,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_gender=StringVar(roota)
    r2 = tkinter.Radiobutton(frame1, text="Female", variable=app_gender, value="F")
    r1 = tkinter.Radiobutton(frame1, text="Male", variable=app_gender, value="M")
    
    age=tkinter.Label(frame1, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_age=tkinter.Entry(frame1,width=25)

    c1=tkinter.Label(frame1, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_contact=tkinter.Entry(frame1,width=25)
    


    d=date.today()   
    dat=tkinter.Label(frame1, text="DATE OF APPOINTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_date=tkinter.Entry(frame1,width=25)
    app_date.insert(0, d)
    
    time=tkinter.Label(frame1, text="TIME OF APPOINTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    app_time=tkinter.Entry(frame1,width=25)
    app_time.insert(0, current_time)
    
    ct=tkinter.Label(frame1,text="CONSULTING DOCTOR",font=("Arial",12,"bold"), fg="#022B63", bg="white")

    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    c.execute("select name from employee where department='Doctor';")
    rows=c.fetchall()

    L=[]
    for row in rows:
        L.insert(0,row[0])
        
    d_sel=tkinter.StringVar(roota)
    d_sel.set(L[0])

    app_CT=tkinter.OptionMenu(frame1, d_sel, *L) #app_dept is a tkinter variable and * is used in python when unpacking is required
    
        
    depts=["General_Physician","Chest_Physician","Paediatrician","General_Surgeon","Cardiologist"]
    app_dept=tkinter.StringVar(roota)
    app_dept.set(depts[0])
    dept=tkinter.Label(frame1,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    app_d=tkinter.OptionMenu(frame1, app_dept, *depts) #app_dept is variable and * is used in python when unpacking is required
    app_d.config(width=20)

    fee=tkinter.Label(frame1,text="CONSULTATION FEE(Rs.)",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    fee_l=[300,500,1000]
    fee_var=StringVar(roota)
    fee_var.set(fee_l[0])
    app_fee=tkinter.OptionMenu(frame1, fee_var, *fee_l)
 
    SUBMIT=tkinter.Button(frame1,text="SUBMIT",command=IN_PAT,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)
    back=tkinter.Button(frame1,text="BACK",command=roota.destroy,font=("Arial",12,"bold"), fg="white", bg="#022B63")    #,bd=0)

    empty=tkinter.Label(frame1, text="   ", font=("Arial",12,"bold"), bg="#022B63", height=2)
    
    regform.grid(row=0, column=0,columnspan=5)
    qn.grid(row = 1, column = 0, pady=5, padx=30,)
    app_qn.grid(row = 2, column = 0, pady=5, padx=30,)  
    name.grid(row = 1, column = 1, pady=5, padx=30,)
    app_name.grid(row = 2, column = 1, pady=5, padx=30,)
    gender.grid(row = 1, column = 2, pady=5, padx=30,)
    r1.grid(row = 2, column = 2, pady=5, padx=30,sticky=E)
    r2.grid(row = 2, column = 2, pady=5, padx=30,sticky=W)
    age.grid(row = 1, column = 3, pady=5, padx=30,)
    app_age.grid(row = 2, column = 3, pady=5, padx=30,)
    c1.grid(row = 1, column = 4, pady=5, padx=30,)
    app_contact.grid(row = 2, column = 4, pady=5, padx=30,)

    empty.grid(row=3, column=0, columnspan=5)
    
    dat.grid(row = 4, column = 0, pady=5, padx=30,)
    app_date.grid(row = 5, column = 0, pady=5, padx=30,)
    time.grid(row = 4, column = 1, pady=5, padx=30,)
    app_time.grid(row = 5, column = 1, pady=5, padx=30,)
    ct.grid(row = 4, column = 2, pady=5, padx=30, )
    app_CT.grid(row = 5, column = 2, pady=5, padx=30,)
    dept.grid(row = 4, column = 3, pady=5, padx=30,)
    app_d.grid(row = 5, column = 3, pady=5, padx=30,)
    fee.grid(row = 4, column = 4, pady=5, padx=30,)
    app_fee.grid(row = 5, column = 4, pady=5, padx=30,)

    SUBMIT.grid(row = 6, column = 4)
    back.grid(row = 6, column = 1)

    roota.iconbitmap('logo.ico')
    roota.title("V tReat_app_form")
    roota.geometry("1199x600+100+50")


    roota.mainloop()


#input appointments form
def IN_PAT():
    global aa1, aa2, aa3, aa4, aa5, aa6, aa7, aa8, aa9,conn
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()

    aa1=app_name.get()
    aa2=str(app_gender.get())
    aa3=app_age.get()
    aa4=app_contact.get()
    aa5=app_qn.get()
    aa6=app_date.get()
    aa7=app_time.get()
    aa8=d_sel.get()
    aa9=app_dept.get()
    aa10=fee_var.get()


    c.execute('INSERT INTO appointments(name,gender,age,contact,queue_no,app_date,app_time, doctor, department, c_fee) VALUES("{}","{}",{},{},{},"{}","{}","{}","{}".{})'.format(aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10))
    roota.destroy()
    tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM","APPOINTMENT BOOKED IN DATABASE")
    conn.commit()
    conn.close()
    
    



#exit from appointments form
def EXO():
    roota.destroy()

#function for appointments form help
def hp():
    tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM","For any help regarding the software \n CONTACT the creators using the details given in the About Section")

def ab():
   tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM"," The software is designed and created by \n \n Vihaan S. Kumar Contact-456789xxxx\n Rohan Nag Contact-789659xxxx \n \n Email- pydeveloper@gmail.com \n \n©2020")




'''=====================================================================PATDELSU_CODE====================================================================='''


#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10
    global l1,l2,l3,l4,l5,l6,l7,l8,l9
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    frameS.place_forget() #forget hides the frame

    if (s_var.get()=="ID"):
        inp_s=int(entry.get())
        c.execute('select * from appointments where app_id=%d;'%inp_s)
        p=c.fetchall()
    elif (s_var.get()=="NAME"):
        c.execute('select * from appointments where name=%s;'%entry.get())
        p=c.fetchall()
    elif (s_var.get()=="DOCTOR"):
        c.execute('select * from appointments where doctor=%s;'%d_sel.get())
        p=c.fetchall()
        
    if (len(p)==0):
        messagebox.showerror("Error","NO APOINTMENTS WITH SUCH ID/NAME;", parent=rootS)
    else:
        c.execute('SELECT * FROM APPOINTMENTS where app_id=%d;'%inp_s)
        t=c.fetchall()
        for i in t:
            app_det=tkinter.Label(rootS,text="APPOINTMENTS DETAILS",font="Arial 24 bold",fg="light gray", bg="#022B63")
            l1=tkinter.Label(rootS,text="APPOINTMENT ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="QUEUE NO.",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis6=tkinter.Label(rootS,text=i[5])
            l7=tkinter.Label(rootS,text="APPOINTMENT DATE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis7=tkinter.Label(rootS,text=i[6])
            l8=tkinter.Label(rootS,text="APPOINTMENT TIME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis8=tkinter.Label(rootS,text=i[7])
            l9=tkinter.Label(rootS,text="CONSULTING DOCTOR ",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis9=tkinter.Label(rootS,text=i[8])
            l10=tkinter.Label(rootS,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis10=tkinter.Label(rootS,text=i[9])


            app_det.grid(row=0, column=0, pady=5, padx=2,columnspan=2)
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

            conn.commit()


def eXO():
    rootS.destroy()

##search window
def A_Display():
    global rootS,head,entry,searchB, frameS, s_var,d_sel
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    frameS=tkinter.Frame(rootS)
    
    head=tkinter.Label(frameS,text="Search Using:",font="Arial 12 bold",fg="light gray", bg="#022B63")
    list=["NAME", "ID","DOCTOR"]
    s_var=StringVar(rootS)
    searchL=tkinter.OptionMenu(frameS, s_var, *list)
    data=tkinter.Label(frameS, text="Enter the Search ID/Name")
    entry=tkinter.Entry(frameS)
    searchB=tkinter.Button(frameS,text='SEARCH',command=Search_button)

    def field():
        if s_var.get()=="DOCTOR":
            conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
            c=conn.cursor()
            c.execute("select name from employee where department='Doctor';")
            rows=c.fetchall()

            d_sel=tkinter.StringVar(rootS)
            d_sel.set(rows[0])
            app_CT=tkinter.OptionMenu(frameS, d_sel, *rows)
            app_CT.grid(row=2,column=0)
            searchB.grid(row=3,column=0,columnspan=3)
            
        elif (s_var.get()=="ID") or (s_var.get()=="NAME"):
            data.grid(row=1, column=0)
            entry.grid(row=1,column=1)
            searchB.grid(row=3,column=0,columnspan=3)
        
    
    bt=tkinter.Button(frameS, text='Confirm Field',command=field)
    s_var.set("Select the desired Field")


    
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=A_Display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    
    
    head.grid(row=0,column=0)
    searchL.grid(row=0,column=1)
    bt.grid(row=0, column=2)
    frameS.place(x=0,y=0)
    rootS.mainloop()


#DELETE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    inp_d = int(entry1.get())
    c.execute("select * from APPOINTMENTS where app_id=%d;"%inp_d)
    p=c.fetchall()
    if (len(p)==0):
        tkinter.messagebox.showerror("VtReat Database System", "The appointment id is not valid.")

    else:
        c.execute('DELETE FROM APPOINTMENTS where app_id=%d;'%inp_d)
        tkinter.messagebox.showinfo("VtReat Database System", "The appointment has been permanently deleted")
        conn.commit()
        rootD.destroy()
        rootP.destroy()
        


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="ENTER PATIENT ID TO DELETE",fg="blue")
    entry1=tkinter.Entry(rootD)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button)
    headD.pack()
    entry1.pack()
    DeleteB.pack()
    rootD.mainloop()




##-----APPOINTMENTS UPDATE SCREEN -----##
def A_UPDATE():
    global appu_ID,appu_name, appu_gender, appu_age,appu_date,appu_contact,appu_CT, n,appu_dept,appu_qn, appu_time, feeu_var
    global rootU, regform, id, name, dob, gender, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.title("APPOINTMENT UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Help", command=hp)
    filemenu.add_command(label="About", command=ab)
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
     
    def Pupdate_box():
        global appu_ID,appu_name, appu_gender, appu_age,appu_date,appu_contact,appu_CT, n,appu_dept,appu_qn, appu_time, feeu_var
        conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
        c=conn.cursor()
        n=int(appu_ID.get())
        c.execute('Select * from APPOINTMENTS where app_id=%d'%n)
        p=c.fetchall()
        if ((len(p))!=0):
            name=tkinter.Label(rootU,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_name = tkinter.Entry(rootU,width=50)
            
            gender=tkinter.Label(rootU,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_gender=tkinter.Listbox(rootU,selectmode='SINGLE', exportselection=0, height=1, width=50)
            appu_gender.insert(tkinter.END, "M")
            appu_gender.insert(tkinter.END, "F")

            age=tkinter.Label(rootU, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_age=tkinter.Entry(rootU,width=50)

            c1=tkinter.Label(rootU, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_contact=tkinter.Entry(rootU,width=50)

            qn=tkinter.Label(rootU, text="QUEUE NO.",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_qn=tkinter.Entry(rootU,width=50)
            
            date=tkinter.Label(rootU, text="APPOINTMENT DATE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_date=tkinter.Entry(rootU, width=50)         

            time=tkinter.Label(rootU, text="APPOINTMENT TIME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_time=tkinter.Entry(rootU,width=50)

            ct=tkinter.Label(rootU,text="CONSULTING DOCTOR",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            appu_CT=tkinter.Entry(rootU,width=50)

            dept=tkinter.Label(rootU,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            depts=["General_Physician","Chest_Physician","Paediatrician","General_Surgeon","Cardiologist"]
            appu_dept=tkinter.StringVar(rootU)
            appu_d=tkinter.OptionMenu(rootU, appu_dept, *depts) 
            appu_d.config(width=20)

            fee=tkinter.Label(rootU,text="CONSULTATION FEE(Rs.)",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            fee_l=[300,500,1000]
            feeu_var=StringVar(rootU)
            appu_fee=tkinter.OptionMenu(rootU, feeu_var, *fee_l)


            c.execute('Select * from APPOINTMENTS where app_id={};'.format(appu_ID.get()))
            t=c.fetchall()
            for i in t:
                appu_name.insert(0,i[1])
                appu_gender.insert(0,i[2])
                appu_age.insert(0,i[3])
                appu_contact.insert(0,i[4])
                appu_qn.insert(0,i[5])
                appu_date.insert(0,i[6])
                appu_time.insert(0,i[7])
                appu_CT.insert(0,i[8])
                appu_dept.set(i[9])
                feeu_var.set(i[10])

            UPDATE=tkinter.Button(rootU,text="UPDATE",command=up1,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)
            
            name.grid(row = 2, column = 0, pady=5,sticky=W)
            appu_name.grid(row = 2, column = 1, pady=5)
            gender.grid(row = 3, column = 0, pady=5,sticky=W)
            appu_gender.grid(row = 3, column = 1, pady=5)
            age.grid(row = 4, column = 0, pady=5,sticky=W)
            appu_age.grid(row = 4, column = 1, pady=5)
            c1.grid(row = 5, column = 0, pady=5,sticky=W)
            appu_contact.grid(row = 5, column = 1, pady=5)
            qn.grid(row = 6, column = 0, pady=5,sticky=W)
            appu_qn.grid(row = 6, column = 1, pady=5)
            date.grid(row=7, column=0,pady=5,sticky=W)
            appu_date.grid(row = 7, column = 1, pady=5)
            time.grid(row=8, column=0,pady=5,sticky=W)
            appu_time.grid(row =8, column = 1, pady=5)
            ct.grid(row = 9, column = 0, pady=5, padx=2, sticky=W)
            appu_CT.grid(row = 9, column = 1, pady=5)
            dept.grid(row = 10, column = 0, pady=5,sticky=W)
            appu_d.grid(row = 10, column = 1, pady=5)
            fee.grid(row = 11, column = 0, pady=5,sticky=W)
            appu_fee.grid(row = 11, column = 1, pady=5)
            
            UPDATE.grid(row = 12, column = 0)
        else:
            tkinter.messagebox.showerror("V tReat DATABSE SYSTEM", "APPOINTMENT NOT BOOKED")

    upform=tkinter.Label(rootU,text="UPDATE FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")
    id=tkinter.Label(rootU,text="ID OF PATIENT TO UPDATE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    appu_ID=tkinter.Entry(rootU,width=50)
    id_bt=tkinter.Button(rootU, text="Search",command=Pupdate_box,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=23)



    
    upform.grid(row=0, column=0,columnspan=2)
    id.grid(row = 1, column = 0, pady=5,sticky=W)
    appu_ID.grid(row = 1, column = 1, pady=5)
    id_bt.grid(row = 1, column = 2, pady=5)

    rootU.mainloop()

#Update command of button
def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    u1=appu_ID.get()
    u2=appu_name.get()
    u3=appu_gender.get(tkinter.ACTIVE)
    u4=appu_age.get()
    u5=appu_contact.get()
    u6=appu_qn.get()
    u7=appu_date.get()
    u8=appu_time.get()
    u9=appu_CT.get()
    u10=appu_dept.get()
    u11=feeu_var.get()

    c.execute('UPDATE APPOINTMENTS SET name="{}",gender="{}",age={},contact={},queue_no={},app_date="{}",app_time="{}", doctor="{}", department="{}", c_fee={} where app_id={};'.format( u2, u3, u4, u5, u6,u7,u8,u9,u10,u11,u1))  
    tkinter.messagebox.showinfo("V tReat DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
    conn.commit()
    rootU.destroy()


def EXITT():
    rootU.destroy()

