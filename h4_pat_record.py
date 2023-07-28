import pymysql
import tkinter
from tkinter import*
import tkinter.messagebox
from datetime import date
from h3_pat_form import hp,ab


P_id=None
rootR=None

#Surgery Insert Button
def sinsert_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn,cst
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    if surg_var.get()=="Knee_Replacement":
        cst=230000
    elif surg_var.get()=="Kidney_Transplant":
        cst=500000
    elif surg_var.get()=="Tonsil_Surgery":
        cst=100000
    elif surg_var.get()=="Angioplasty":
        cst=120000
    elif surg_var.get()=="Coronary_Artery_Bypass":
        cst=150000
    elif surg_var.get()=="Laparoscopic_Cholecystectomy":
        cst=50000
    r1=P_id.get()
    r2=surg_var.get()
    r3=sdat.get()
    r4=cst
    c.execute('INSERT INTO sur_test VALUES({},"{}","{}",{});'.format(r1,r2,r3,r4))
    tkinter.messagebox.showinfo("VtReat Database System", "Surgery added to Database")
    conn.commit()
    conn.close()
    ins.grid_forget()
    sdat.config(state='disabled')
    surg.config(state='disabled')

    
#Test Insert Button
def tinsert_button():
    global cst
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    if test_var.get()=="Biochemistry_Test":
        cst=800
    elif test_var.get()=="Haematology_Test":
        cst=1000
    elif test_var.get()=="X-Ray":
        cst=500
    elif test_var.get()=="CT_Scan":
        cst=1700
    elif test_var.get()=="Thyroid_Test":
        cst=400
    elif test_var.get()=="Insulin":
        cst=200
    elif test_var.get()=="COVID_RTPCR":
        cst=1200
    elif test_var.get()=="COVID_Antibody":
        cst=1000
    elif test_var.get()=="Antigen_Test":
        cst=1200
    elif test_var.get()=="Sonography":
        cst=1700
    elif test_var.get()=="ECG":
        cst=500
    r1=P_id.get()
    r2=test_var.get()
    r3=tdat.get()
    r4=cst
    c.execute('INSERT INTO sur_test VALUES({},"{}","{}",{});'.format(r1,r2,r3,r4))
    tkinter.messagebox.showinfo("VtReat Database System", "Test added to Database")
    conn.commit()
    conn.close()
    ins.grid_forget()
    tdat.config(state='disabled')
    test.config(state='disabled')



def exitt():
    rootR.destroy()



#Surgery/Test Window
def SUR_TEST():
    global rootR,r_head,P_id,id,da_l,da ,dd_l,dd,Submit,Update,cr,a,surg_var, sdat,a,test_var,tdat,a,cst
    rootR=tkinter.Tk()
    rootR.title("PATIENT RECORD")
    rootR.geometry("800x800")
    rootR.iconbitmap('logo.ico')
    
    menubar=tkinter.Menu(rootR)
    filemenu=tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New",command=SUR_TEST)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exitt)

    helpmenu=tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help",command=hp)
    helpmenu.add_command(label="About",command=ab)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootR.config(menu=menubar)
    
    r_head=tkinter.Label(rootR,text="PATIENT RECORD",font="Arial 24 bold",fg="light gray", bg="#022B63")

    id=tkinter.Label(rootR,text="PATIENT ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    P_id=tkinter.Entry(rootR)
    surg_list=["Knee_Replacement","Kidney_Transplant","Tonsil_Surgery","Angioplasty","Coronary_Artery_Bypass","Laparoscopic_Cholecystectomy"]
    test_list=["Biochemistry_Test","Haematology_Test","X-Ray", "CT_Scan", "Thyroid_Test","Insulin","COVID_RTPCR","COVID_Antibody","Antigen_Test","Sonography","ECG"]

    a=7
    def new_surg():
        global surg_var, sdat,a,cst,surg_list, ins, surg
        surgl=tkinter.Label(rootR, text="SURGERY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        surg_var=tkinter.StringVar(rootR)
        surg_list=["Knee_Replacement","Kidney_Transplant","Tonsil_Surgery","Angioplasty","Coronary_Artery_Bypass","Laparoscopic_Cholecystectomy"]
        surg=tkinter.OptionMenu(rootR, surg_var, *surg_list)
        surg_var.set("N/A")

        s_date=tkinter.Label(rootR, text="Date of Surgery",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        d=date.today()
        sdat=tkinter.Entry(rootR)
        sdat.insert(tkinter.END, d)
        ins=tkinter.Button(rootR, text="INSERT", command=sinsert_button,font=("Arial",12,"bold"), fg="white", bg="#022B63")
        
        surgl.grid(row=a , column=1, stick=W, padx=5)
        surg.grid(row=a , column=2)
        s_date.grid(row=a , column=3)
        sdat.grid(row=a ,column=4)
        ins.grid(row=a , column=5)
        a=a+1

                   
    def new_test():
        global test_var,tdat,a,cst,test_list, ins,test
        testl=tkinter.Label(rootR, text="LAB TESTS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        test_var=tkinter.StringVar(rootR)
        test_var.set("N/A")        
        test_list=["Biochemistry_Test","Haematology_Test","X-Ray", "CT_Scan", "Thyroid_Test","Insulin","COVID_RTPCR","COVID_Antibody","Antigen_Test","Sonography","ECG"]
        test=tkinter.OptionMenu(rootR, test_var, *test_list)
        t_date=tkinter.Label(rootR, text="Date of Test",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        d=date.today()
        tdat=tkinter.Entry(rootR)
        tdat.insert(tkinter.END, d)
        ins=tkinter.Button(rootR, text="INSERT", command=tinsert_button,font=("Arial",12,"bold"), fg="white", bg="#022B63")
        testl.grid(row=a , column=1,padx=5)
        test.grid(row=a , column=2)
        t_date.grid(row=a , column=3)
        tdat.grid(row=a ,column=4)
        ins.grid(row=a , column=5)
        a=a+1
        

    def extract():
        global a
        P_id.config(state='disabled')
        s_add=tkinter.Button(rootR, text="Add Surgery", command=new_surg,font=("Arial",12,"bold"), fg="white", bg="#022B63")
        t_add=tkinter.Button(rootR, text="Add Test", command=new_test,font=("Arial",12,"bold"), fg="white", bg="#022B63")
        s_add.grid(row=6,column=2,pady=5)
        t_add.grid(row=6,column=4,pady=5)

        conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
        c=conn.cursor()
        c.execute("select name,gender,age,`test/surgery`,`date_sur/test` from PATIENT left join sur_test on patient.id=sur_test.id where patient.id=%d;"%int(P_id.get()))
        rows=c.fetchall()

        for row in rows:
            if row[3] in surg_list:
                surgl=tkinter.Label(rootR, text="SURGERY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                surg=tkinter.Label(rootR, text=row[3])
                s_date=tkinter.Label(rootR, text="Date of Surgery",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                date=tkinter.Label(rootR, text=row[4])
                surgl.grid(row=a , column=1, stick=W, padx=5)
                surg.grid(row=a , column=2)
                s_date.grid(row=a , column=3)
                date.grid(row=a ,column=4)
                a=a+1

            elif row[3] in test_list:
                testl=tkinter.Label(rootR, text="LAB TESTS",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                test=tkinter.Label(rootR, text=row[3])
                t_date=tkinter.Label(rootR, text="Date of Test",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                date=tkinter.Label(rootR, text=row[4])
                testl.grid(row=a , column=1, stick=W, padx=5)
                test.grid(row=a , column=2)
                t_date.grid(row=a , column=3)
                date.grid(row=a ,column=4)                
                a=a+1

            if len(rows)!=0:
                namel=tkinter.Label(rootR,text="PATIENT NAME:",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                name=tkinter.Label(rootR,text=row[0])
                genderl=tkinter.Label(rootR,text="GENDER:",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                gender=tkinter.Label(rootR,text=row[1])
                agel=tkinter.Label(rootR,text="AGE:",font=("Arial",12,"bold"), fg="#022B63", bg="white")
                age=tkinter.Label(rootR,text=row[2])        
                namel.grid(row=1, column=2, padx=5)
                name.grid(row=1, column=3, padx=5)
                genderl.grid(row=1, column=4, padx=5)
                gender.grid(row=1, column=5, padx=5)
                agel.grid(row=1, column=6, padx=5)
                age.grid(row=1, column=7, padx=5)
            else:
                tkinter.messagebox.showerror("VtReat Database System","No patient with such ID")

    bt=tkinter.Button(rootR, text="Confirm", command=extract)
    empty=tkinter.Label(rootR, text="  ", height=2)

    

        



    r_head.grid(row=0,column=0, columnspan=8)
    id.grid(row=1,column=0,pady=5)
    P_id.grid(row=1,column=1,pady=5)
    bt.grid(row=2, column=0)
    empty.grid(row=5,column=0,columnspan=8)


    
    
    
    rootR.mainloop()
