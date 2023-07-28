from tkinter import*
import tkinter 
from PIL import ImageTk
import pymysql
from tkinter import ttk
import datetime



def PAT():
    global pat_address, pat_contact, pat_age, pat_CT, pat_date, pat_email, pat_ID, pat_name, pat_Gender, pat_cat, pat_dept, room_var, room_no, rate, d_sel
    global rootp,regform,id,name,Gender,email,ct,addr,c1,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE, r4, L1
    
    class Table:
        def __init__(self,rootp):
            self.rootp=rootp
            
            
            frame1=Frame(self.rootp, bg='#022B63', borderwidth=1)
            frame1.place(relx=0.5, relheight=1, relwidth=0.5)
            scroll_x=Scrollbar(frame1, orient=HORIZONTAL)
            scroll_y=Scrollbar(frame1, orient=VERTICAL)
            self.pat_table=ttk.Treeview(frame1, columns=("id", "name", "Gender", "age","date/time","Phno","address","email","doctor","department","categ","roomt","roomno","roomc"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.pat_table.xview)
            scroll_y.config(command=self.pat_table.yview)
            self.pat_table.heading("id",text="Patient ID")
            self.pat_table.heading("name",text="Name")
            self.pat_table.heading("Gender",text="Gender")
            self.pat_table.heading("age",text="Age")
            self.pat_table.heading("date/time",text="Date/Time")
            self.pat_table.heading("Phno",text="Contact Number")
            self.pat_table.heading("address",text="Address")
            self.pat_table.heading("email",text="Email-ID")
            self.pat_table.heading("doctor",text="Consulting Team/Doctor")
            self.pat_table.heading("department",text="Department")
            self.pat_table.heading("categ",text="Patient Category")
            self.pat_table.heading("roomt",text="Room Type")
            self.pat_table.heading("roomno",text="Room No.")
            self.pat_table.heading("roomc",text="Room Charges")
            self.pat_table['show']='headings'
            self.pat_table.pack()
            conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
            c=conn.cursor()
            c.execute("select* from PATIENT")
            rows=c.fetchall()
            if len(rows)!=0:
                self.pat_table.delete(*self.pat_table.get_children())
                for row in rows:
                    self.pat_table.insert("",END,values=row)
                print("Data inserted in treeview from vtreat database")
                conn.commit()
                conn.close()
                
            else:
                print("Not done")



    rootp=Tk()
    call=Table(rootp)
    rootp.title("PATIENT FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=EXO)

    emenu=tkinter.Menu(menubar, tearoff=0)
    emenu.add_command(label="Update",command=P_UPDATE)
    emenu.add_separator()
    emenu.add_command(label="Search", command=P_display)
    emenu.add_separator()
    emenu.add_command(label="Delete", command=D_display)

    helpmenu=tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help",command=hp)
    helpmenu.add_command(label="About",command=ab)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=emenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)

    frame2=Frame(rootp, bg='#022B63')
    frame2.place(x=0, y=0, relheight=1, relwidth=0.5)

    regform=tkinter.Label(frame2,text="REGISTRATION FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")

    id=tkinter.Label(frame2,text="PATIENT ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_ID=tkinter.Entry(frame2,width=50)
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    c.execute("select max(id) from PATIENT;")
    i=c.fetchone()
    i=i[0]+1
    pat_ID.insert(tkinter.END, i)
    pat_ID.config(state='disabled')

    name=tkinter.Label(frame2,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_name = tkinter.Entry(frame2,width=50)

    Gender=tkinter.Label(frame2,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_Gender=tkinter.Listbox(frame2,selectmode='SINGLE', exportselection=0, height=2, width=50)
    pat_Gender.insert(tkinter.END, "M")
    pat_Gender.insert(tkinter.END, "F")

    age=tkinter.Label(frame2, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_age=tkinter.Entry(frame2,width=50)

    def  add_date():
        global pat_date,now
        now = datetime.datetime.now()
        pat_date=now.strftime("%Y-%m-%d %H:%M:%S")
        datet=tkinter.Label(frame2, text=pat_date,width=25)
        datet.grid(row = 5, column = 1)
        
    date=tkinter.Label(frame2, text="DATE/TIME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    dt_bt=tkinter.Button(frame2,text="Add current date/time",command=add_date,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=23)
    




    c1=tkinter.Label(frame2, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_contact=tkinter.Entry(frame2,width=50)

    addr=tkinter.Label(frame2, text="ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_address=tkinter.Entry(frame2,width=50)

    email=tkinter.Label(frame2, text="EMAIL",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_email = tkinter.Entry(frame2,width=50)

    ct=tkinter.Label(frame2,text="CONSULTING TEAM / DOCTOR",font=("Arial",12,"bold"), fg="#022B63", bg="white")            

    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    c.execute("select name from employee where department='Doctor';")
    rows=c.fetchall()

    L=[]
    for row in rows:
        L.insert(0, row[0])
        
    d_sel=tkinter.StringVar(rootp)
    d_sel.set(L[0])
    pat_CT=tkinter.OptionMenu(frame2, d_sel, *L) #app_dept is a tkinter variable and * is used in python when unpacking is required

    
    dept=tkinter.Label(frame2,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_dept = tkinter.Listbox(frame2, selectmode='SINGLE', exportselection=0, height=5, width=50)
    pat_dept.insert(tkinter.END, "General_Physician")
    pat_dept.insert(tkinter.END, "Chest_Physician")
    pat_dept.insert(tkinter.END, "Paediatrician")
    pat_dept.insert(tkinter.END, "General_Surgeon")
    pat_dept.insert(tkinter.END, "Cardiologist")

    cat=tkinter.Label(frame2, text="PATIENT CATEGORY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_cat=tkinter.Listbox(frame2, selectmode='SINGLE', exportselection=0, height=3, width=50)
    pat_cat.insert(tkinter.END, "General")
    pat_cat.insert(tkinter.END, "Critical")
    pat_cat.insert(tkinter.END, "Emergency")

    def room_sel(event):
        global r4,L1
        r2=room_var.get()
        if r2=='Deluxe_Single_Room':
            room_no.delete(0,tkinter.END)
            L1=[101,102,201,202,301,302]
            r4=8000
            for j in L1:
                room_no.insert(tkinter.END,j)
            rate.config(text=r4)
        elif r2=='Single_Room':
            room_no.delete(0,tkinter.END)
            L1=[111,112,211,212,311,312]
            r4=6000
            for j in L1:
                room_no.insert(tkinter.END,j)
            rate.config(text=r4)
        elif r2=='Double_Room':
            room_no.delete(0,tkinter.END)
            L1=[121,122,221,222,321,322]
            r4=5000
            for j in L1:
                room_no.insert(tkinter.END,j)
            rate.config(text=r4)
        elif r2=='Triple_Room':
            room_no.delete(0,tkinter.END)
            L1=[131,132,231,232,331,332]
            r4=3000
            for j in L1:
                room_no.insert(tkinter.END,j)
            rate.config(text=r4)
        elif r2=='General_Ward':
            room_no.delete(0,tkinter.END)
            L1=[141,142,241,242,341,342]
            r4=2000
            for j in L1:
                room_no.insert(tkinter.END,j)
            rate.config(text=r4)
    room_tl=tkinter.Label(frame2,text="ROOM TYPE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    L=['Deluxe_Single_Room','Single_Room','Double_Room','Triple_Room','General_Ward']
    room_var=tkinter.StringVar(frame2)
    room_t= tkinter.OptionMenu(frame2, room_var, *L,command=room_sel)

    
    room_nol=tkinter.Label(frame2,text="ROOM NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    room_no = tkinter.Listbox(frame2, width=8, height=1, selectmode='SINGLE', exportselection=0)
   
    ratel=tkinter.Label(frame2, text="ROOM CHARGES",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    rate=tkinter.Label(frame2,text="------")

    
    back=tkinter.Button(frame2,text="BACK",command=rootp.destroy,font=("Arial",12,"bold"), fg="white", bg="#022B63")    #,bd=0)
    SUBMIT=tkinter.Button(frame2,text="SUBMIT",command=IN_PAT,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)

    
    regform.grid(row=0, column=0,columnspan=2)
    id.grid(row = 1, column = 0, pady=5,sticky=W)
    pat_ID.grid(row = 1, column = 1, pady=5)
    name.grid(row = 2, column = 0, pady=5,sticky=W)
    pat_name.grid(row = 2, column = 1, pady=5)
    Gender.grid(row = 3, column = 0, pady=5,sticky=W)
    pat_Gender.grid(row = 3, column = 1, pady=5)
    age.grid(row = 4, column = 0, pady=5,sticky=W)
    pat_age.grid(row = 4, column = 1, pady=5)
    date.grid(row = 5, column = 0, pady=5,sticky=W)
    dt_bt.grid(row = 5, column = 1, pady=5)
    c1.grid(row = 6, column = 0, pady=5,sticky=W)
    pat_contact.grid(row = 6, column = 1, pady=5)
    addr.grid(row = 7, column = 0, pady=5,sticky=W)
    pat_address.grid(row = 7, column = 1, pady=5)
    email.grid(row = 8, column = 0, pady=5,sticky=W)
    pat_email.grid(row = 8, column = 1, pady=5)
    ct.grid(row = 9, column = 0, pady=5, padx=2, sticky=W)
    pat_CT.grid(row = 9, column = 1, pady=5)
    dept.grid(row = 10, column = 0, pady=5,sticky=W)
    pat_dept.grid(row = 10, column = 1, pady=5)
    cat.grid(row = 11, column = 0, pady=5,sticky=W)
    pat_cat.grid(row = 11, column = 1, pady=5)
    room_tl.grid(row = 12, column = 0, pady=5,sticky=W)
    room_t.grid(row = 12, column = 1, pady=5)
    room_nol.grid(row = 13, column = 0, pady=5,sticky=W)
    room_no.grid(row = 13, column = 1, pady=5)
    ratel.grid(row = 14, column = 0, pady=5,sticky=W)
    rate.grid(row = 14, column = 1, pady=5)

    SUBMIT.grid(row = 15, column = 0)
    back.grid(row = 15, column = 1)

    rootp.iconbitmap('logo.ico')
    rootp.title("V tReat_pat_form")
    rootp.geometry("1199x600+100+50")


    rootp.mainloop()

#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, ce1,conn
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_Gender.get(tkinter.ACTIVE)
    pp4=pat_age.get()
    pp5=pat_date
    pp6=pat_contact.get()
    pp7=pat_address.get()
    pp8=pat_email.get()
    pp9=d_sel.get()
    pp10=pat_dept.get(tkinter.ACTIVE)
    pp11=pat_cat.get(tkinter.ACTIVE)
    pp12=room_var.get()
    pp13=room_no.get(tkinter.ACTIVE)
    pp14=r4
    

    c.execute('INSERT INTO patient(name,gender,age,date, contact,address,email,doctor,department,category, room_type, room_no, room_price) VALUES("{}","{}",{},"{}",{},"{}","{}","{}","{}","{}","{}",{},{})'.format(pp2,pp3,pp4,pp5,pp6,pp7,pp8,pp9,pp10,pp11,pp12,pp13,pp14))
    rootp.destroy()
    tkinter.messagebox.showinfo("V tReat DATABASE SYSTEM","PATIENT REGISTERED IN DATABASE")
    conn.commit()
    conn.close()# it flushes the memory
    
    



#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
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
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10, dis11
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    frameS.place_forget() #forget hides the frame
    
    
    if searchL.get(tkinter.ACTIVE)=="Name":
        z=str(entry.get())
        c.execute('select * from PATIENT where name="{}";'.format(z))
        t=c.fetchall()        
    elif (searchL.get(tkinter.ACTIVE)=="ID"):
        inp_s=int(entry.get())
        c.execute('select * from PATIENT where ID=%d;'%inp_s)
        t=c.fetchall()
    if (len(t)==0):
        messagebox.showerror("Error","NO PATIENT WITH SUCH ID/NAME;", parent=rootS)
    else:
        for i in t:
            pat_det=tkinter.Label(rootS,text="PATIENT DETAILS",font="Arial 24 bold",fg="light gray", bg="#022B63")
            l1=tkinter.Label(rootS,text="PATIENT ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="PATIENT AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="DATE OF REGISTRATION",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="PATIENT CONTACT_NO",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis6=tkinter.Label(rootS,text=i[5])
            l7=tkinter.Label(rootS,text="PATIENT ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis7=tkinter.Label(rootS,text=i[6])
            l8=tkinter.Label(rootS,text="PATIENT EMAIL-ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis8=tkinter.Label(rootS,text=i[7])
            l9=tkinter.Label(rootS,text="CONSULTING TEAM/DOCTOR ",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis9=tkinter.Label(rootS,text=i[8])
            l10=tkinter.Label(rootS,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis10=tkinter.Label(rootS,text=i[9])
            l11=tkinter.Label(rootS,text="CATEGORY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis11=tkinter.Label(rootS,text=i[10])
            l12=tkinter.Label(rootS,text="ROOM TYPE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis12=tkinter.Label(rootS,text=i[11])
            l13=tkinter.Label(rootS,text="ROOM NO",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis13=tkinter.Label(rootS,text=i[12])
            l14=tkinter.Label(rootS,text="ROOM CHARGES",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            dis14=tkinter.Label(rootS,text=i[13])
            
            pat_det.grid(row=0, column=0, pady=5, padx=2,columnspan=2)
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
            l12.grid(row=12, column=0, pady=5, padx=2)
            dis12.grid(row=12, column=1, pady=5, padx=2)
            l13.grid(row=13, column=0, pady=5, padx=2)
            dis13.grid(row=13, column=1, pady=5, padx=2)
            l14.grid(row=14, column=0, pady=5, padx=2)
            dis14.grid(row=14, column=1, pady=5, padx=2)
            conn.commit()


def eXO():
    rootS.destroy()

##search window
def P_display():
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
    filemenu.add_command(label="NEW", command=P_display)
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
    c.execute("select * from PATIENT where ID=%d;"%inp_d)
    p=c.fetchall()
    if (len(p)==0):
        errorD = tkinter.Label(rootD, text="PATIENT RECORD NOT FOUND")
        errorD.pack()
    else:
        c.execute('DELETE FROM PATIENT where ID=%d;'%inp_d)
        tkinter.messagebox.showinfo("VtReat Database System", "The Patient record has been permanently deleted")
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
    rootD.iconbitmap('logo.ico')
    rootD.mainloop()




##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global patu_ID,patu_name, patu_Gender, patu_age,patu_date,patu_contact,patu_address,patu_email,patu_CT, n,patu_dept,patu_cat, roomu_var, r4, L1, roomu_no
    global rootU, regform, id, name, dob, Gender, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
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
        global patu_ID,patu_name, patu_Gender, patu_age,patu_date,patu_contact,patu_address,patu_email,patu_CT, n,patu_dept,patu_cat, roomu_var, roomu_no,r4
        conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
        c=conn.cursor()
        n=int(patu_ID.get())
        c.execute('Select * from PATIENT where id=%d'%n)
        p=c.fetchall()
        if ((len(p))!=0):
            name=tkinter.Label(rootU,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_name = tkinter.Entry(rootU,width=50)
            Gender=tkinter.Label(rootU,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_Gender=tkinter.Listbox(rootU,selectmode='SINGLE', exportselection=0, height=1, width=50)
            patu_Gender.insert(tkinter.END, "M")
            patu_Gender.insert(tkinter.END, "F")

            age=tkinter.Label(rootU, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_age=tkinter.Entry(rootU,width=50)

            date=tkinter.Label(rootU, text="DATE/TIME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_date=tkinter.Entry(rootU, width=50)
            
            def add_date():
                patu_date.delete(0,'end')
                now = datetime.datetime.now()
                datet=now.strftime("%Y-%m-%d %H:%M:%S")
                patu_date.insert(0,datet)
            dt_bt=tkinter.Button(rootU,text="Add current date/time",command=add_date,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=23)
            
            c1=tkinter.Label(rootU, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_contact=tkinter.Entry(rootU,width=50)

            addr=tkinter.Label(rootU, text="ADDRESS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_address=tkinter.Entry(rootU,width=50)

            email=tkinter.Label(rootU, text="EMAIL",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_email = tkinter.Entry(rootU,width=50)

            ct=tkinter.Label(rootU,text="CONSULTING TEAM / DOCTOR",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_CT=tkinter.Entry(rootU,width=50)

            dept=tkinter.Label(rootU,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_dept = tkinter.Listbox(rootU, selectmode='SINGLE', exportselection=0, height=5, width=50)
            patu_dept.insert(tkinter.END, "General_Physician")
            patu_dept.insert(tkinter.END, "Chest_Physician")
            patu_dept.insert(tkinter.END, "Paediatrician")
            patu_dept.insert(tkinter.END, "General_Surgeon")
            patu_dept.insert(tkinter.END, "Cardiologist")

            cat=tkinter.Label(rootU, text="PATIENT CATEGORY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            patu_cat=tkinter.Listbox(rootU, selectmode='SINGLE', exportselection=0, height=3, width=50)
            patu_cat.insert(tkinter.END, "General")
            patu_cat.insert(tkinter.END, "Critical")
            patu_cat.insert(tkinter.END, "Emergency")

            def room_sel(event):
                global r4,L1
                r2=roomu_var.get()
                if r2=='Deluxe_Single_Room':
                    roomu_no.delete(0,tkinter.END)
                    L1=[101,102,201,202,301,302]
                    r4=8000
                    for j in L1:
                        roomu_no.insert(tkinter.END,j)
                    rateu.config(text=r4)
                elif r2=='Single_Room':
                    roomu_no.delete(0,tkinter.END)
                    L1=[111,112,211,212,311,312]
                    r4=6000
                    for j in L1:
                        roomu_no.insert(tkinter.END,j)
                    rateu.config(text=r4)
                elif r2=='Double_Room':
                    roomu_no.delete(0,tkinter.END)
                    L1=[121,122,221,222,321,322]
                    r4=5000
                    for j in L1:
                        roomu_no.insert(tkinter.END,j)
                    rateu.config(text=r4)
                elif r2=='Triple_Room':
                    roomu_no.delete(0,tkinter.END)
                    L1=[131,132,231,232,331,332]
                    r4=3000
                    for j in L1:
                        roomu_no.insert(tkinter.END,j)
                    rateu.config(text=r4)
                elif r2=='General_Ward':
                    roomu_no.delete(0,tkinter.END)
                    L1=[141,142,241,242,341,342]
                    r4=2000
                    for j in L1:
                        roomu_no.insert(tkinter.END,j)
                    rateu.config(text=r4)
            roomu_tl=tkinter.Label(rootU,text="ROOM TYPE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            L=['Deluxe_Single_Room','Single_Room','Double_Room','Triple_Room','General_Ward']
            roomu_var=tkinter.StringVar(rootU)
            roomu_t= tkinter.OptionMenu(rootU, roomu_var, *L,command=room_sel)

            
            roomu_nol=tkinter.Label(rootU,text="ROOM NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            roomu_no = tkinter.Listbox(rootU, width=8, height=1, selectmode='SINGLE', exportselection=0)
           
            rateul=tkinter.Label(rootU, text="ROOM CHARGES",font=("Arial",12,"bold"), fg="#022B63", bg="white")
            rateu=tkinter.Label(rootU,text="------")

            c.execute('Select * from PATIENT where id={};'.format(patu_ID.get()))
            t=c.fetchall()
            for i in t:
                patu_name.insert(0,i[1])
                patu_Gender.insert(0,i[2])
                patu_age.insert(0,i[3])
                patu_date.insert(0,i[4])
                patu_contact.insert(0,i[5])
                patu_address.insert(0,i[6])
                patu_email.insert(0,i[7])
                patu_CT.insert(0,i[8])
                roomu_var.set(i[11])


            UPDATE=tkinter.Button(rootU,text="UPDATE",command=up1,font=("Arial",12,"bold"), fg="white", bg="#022B63")   #,bd=0)
            
            name.grid(row = 2, column = 0, pady=5,sticky=W)
            patu_name.grid(row = 2, column = 1, pady=5)
            Gender.grid(row = 3, column = 0, pady=5,sticky=W)
            patu_Gender.grid(row = 3, column = 1, pady=5)
            age.grid(row = 4, column = 0, pady=5,sticky=W)
            patu_age.grid(row = 4, column = 1, pady=5)
            date.grid(row = 5, column = 0, pady=5,sticky=W)
            dt_bt.grid(row = 5, column = 2, pady=5)
            patu_date.grid(row = 5, column = 1, pady=5)
            c1.grid(row = 6, column = 0, pady=5,sticky=W)
            patu_contact.grid(row = 6, column = 1, pady=5)
            addr.grid(row = 7, column = 0, pady=5,sticky=W)
            patu_address.grid(row = 7, column = 1, pady=5)
            email.grid(row = 8, column = 0, pady=5,sticky=W)
            patu_email.grid(row = 8, column = 1, pady=5)
            ct.grid(row = 9, column = 0, pady=5, padx=2, sticky=W)
            patu_CT.grid(row = 9, column = 1, pady=5)
            dept.grid(row = 10, column = 0, pady=5,sticky=W)
            patu_dept.grid(row = 10, column = 1, pady=5)
            cat.grid(row = 11, column = 0, pady=5,sticky=W)
            patu_cat.grid(row = 11, column = 1, pady=5)
            roomu_tl.grid(row = 12, column = 0, pady=5,sticky=W)
            roomu_t.grid(row = 12, column = 1, pady=5)
            roomu_nol.grid(row = 13, column = 0, pady=5,sticky=W)
            roomu_no.grid(row = 13, column = 1, pady=5)
            rateul.grid(row = 14, column = 0, pady=5,sticky=W)
            rateu.grid(row = 14, column = 1, pady=5)



            
            UPDATE.grid(row = 15, column = 0)
            
        else:
            tkinter.messagebox.showerror("V tReat DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")

    upform=tkinter.Label(rootU,text="UPDATE FORM",font="Arial 24 bold",fg="light gray", bg="#022B63")
    id=tkinter.Label(rootU,text="ID OF PATIENT TO UPDATE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    patu_ID=tkinter.Entry(rootU,width=50)
    id_bt=tkinter.Button(rootU, text="Search",command=Pupdate_box,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=23)



    
    upform.grid(row=0, column=0,columnspan=2)
    id.grid(row = 1, column = 0, pady=5,sticky=W)
    patu_ID.grid(row = 1, column = 1, pady=5)
    id_bt.grid(row = 1, column = 2, pady=5)
    rootU.iconbitmap('logo.ico')
    rootU.mainloop()

#Update command of button
def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    u1=patu_ID.get()
    u2=patu_name.get()
    u3=patu_Gender.get(tkinter.ACTIVE)
    u4=patu_age.get()
    u5=patu_date.get()
    u6=patu_contact.get()
    u7=patu_address.get()
    u8=patu_email.get()
    u9=patu_CT.get()
    u10=patu_dept.get(tkinter.ACTIVE)
    u11=patu_cat.get(tkinter.ACTIVE)
    u12=roomu_var.get()
    u13=roomu_no.get(tkinter.ACTIVE)
    u14=r4
    


    
    c.execute('UPDATE PATIENT SET name="{}",Gender="{}",age={},date="{}", contact={},address="{}",email="{}",doctor="{}",department="{}",category="{}",room_type="{}",room_no={}, room_price={} where id={};'.format( u2, u3, u4, u5, u6,u7,u8,u9,u10,u11,u12,u13,u14,u1))
  
    tkinter.messagebox.showinfo("V tReat DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
    conn.commit()
    rootU.destroy()


def EXITT():
    rootU.destroy()

