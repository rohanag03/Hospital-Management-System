import tkinter
from tkinter import*
import datetime
from datetime import date
import pymysql

def BILL():
    global pat_ID
    rootB=Tk()
    rootB.title("PATIENT BILL")
    
    frame1=Frame(rootB, bg='light gray')
    frame1.place(x=0, y=0, relheight=1, relwidth=1)
    b_head=tkinter.Label(frame1,text="PATIENT BILL",font="Arial 24 bold",fg="light gray", bg="#022B63")
    id=tkinter.Label(frame1,text="PATIENT ID",font=("Arial",12,"bold"), fg="#022B63", bg="white")
    pat_ID=tkinter.Entry(frame1,width=10)


    def details():
        global pat_name,date_ad, datet, cat_var
        
        id_bt.grid_forget()
        conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
        c=conn.cursor()
        c.execute("select* from patient where id=%d;"%int(pat_ID.get()))
        rows=c.fetchall()
        if len(rows)!=0:
            pat_ID.config(state='disabled')
            for row in rows:
                name=tkinter.Label(frame1, text=row[1])
                pat_name=row[1]
                gender=tkinter.Label(frame1, text=row[2])
                age=tkinter.Label(frame1, text=row[3])
                con=tkinter.Label(frame1, text=row[5])
                date_ad=tkinter.Label(frame1, text=row[4])
                ct=tkinter.Label(frame1, text=row[8])
                dept=tkinter.Label(frame1, text=row[9])
        else:
            rootB.destroy()
            tkinter.messagebox.showerror("VtReat Database System","No patient with this ID is registered")

        
        namel=tkinter.Label(frame1,text="PATIENT NAME",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        genderl=tkinter.Label(frame1,text="GENDER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        agel=tkinter.Label(frame1, text="AGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        conl=tkinter.Label(frame1, text="CONTACT NUMBER",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        
        date_adl=tkinter.Label(frame1, text="DATE OF ADMISSION",font=("Arial",12,"bold"), fg="#022B63", bg="white")

        def  add_date():
            global now, pat_date
            dt_bt.grid_forget()
            now = datetime.datetime.now()
            pat_date=now.strftime("%Y-%m-%d %H:%M:%S")
            datet=tkinter.Label(frame1,width=20, text=pat_date)
            datet.grid(row =3, column =3)
            
        date_disl=tkinter.Label(frame1, text="DATE OF DISCHARGE",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        dt_bt=tkinter.Button(frame1,text="Add current date/time",command=add_date,font=("Arial",10,"bold"), fg="white", bg="#022B63",bd=0,width=20)

        catl=tkinter.Label(frame1, text="CATEGORY",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        cat_list=["General","HDFC","Star Health","ICICI","MaxBupa","Bajaj Allianz","Aditya Birla"]
        cat_var=StringVar(rootB)
        cat_var.set(cat_list[0])
        cat=tkinter.OptionMenu(frame1, cat_var, *cat_list)
        
        ctl=tkinter.Label(frame1,text="CONSULTING TEAM / DOCTOR",font=("Arial",12,"bold"), fg="#022B63", bg="white")
        deptl=tkinter.Label(frame1,text="DEPARTMENT",font=("Arial",12,"bold"), fg="#022B63", bg="white")


        def gen_bt():
            global date1
            conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
            c=conn.cursor()
            c.execute("select* from patient where id=%d;"%int(pat_ID.get()))
            rows=c.fetchall()
            for row in rows:
                date1=row[4]
                room_ty=row[11]
                room_no=row[12]
                room_d=room_ty,"//",room_no
                room_p=row[13]

            date2=now.date()
            date1=date1.date()
            print(date1)
            print(date2)
            sno=tkinter.Label(frame1, text="S.No.", font=("Arial",12,"bold"), fg="#022B63", bg="white", width=15)
            content=tkinter.Label(frame1, text="CONTENTS", font=("Arial",12,"bold"), fg="#022B63", bg="white", width=30)
            perday=tkinter.Label(frame1, text="Cost per Day", font=("Arial",12,"bold"), fg="#022B63", bg="white", width=20)
            total=tkinter.Label(frame1, text="TOTAL", font=("Arial",12,"bold"), fg="#022B63", bg="white", width=20)

            no=tkinter.Label(frame1, text=1,font=("Arial",12,"bold"),bg="light gray")
            c_rt=tkinter.Label(frame1, text=room_d,font=("Arial",12,"bold"),bg="light gray")
            price_label=tkinter.Label(frame1, text=room_p,font=("Arial",12,"bold"),bg="light gray")
    
            day=(date2-date1).days
            price=int(room_p*day)
            p=tkinter.Label(frame1, text=price,font=("Arial",12,"bold"),bg="light gray")
            sno.grid(row=8, column=0, padx=3)
            content.grid(row=8, column=1)
            perday.grid(row=8, column=2)
            total.grid(row=8, column=3)
            no.grid(row=9, column=0)
            c_rt.grid(row=9, column=1, stick=W)
            price_label.grid(row=9, column=2)
            p.grid(row=9, column=3)        
            surg_list=["Knee_Replacement","Kidney_Transplant","Tonsil_Surgery","Angioplasty","Coronary_Artery_Bypass","Laparoscopic_Cholecystectomy"]
            test_list=["Biochemistry_Test","Haematology_Test","X-Ray", "CT_Scan", "Thyroid_Test","Insulin","COVID_RTPCR","COVID_Antibody","Antigen_Test","Sonography","ECG"]

            c.execute("Select `test/surgery`,cost from sur_test where id=%d;"%int(pat_ID.get()))
            rows=c.fetchall()
            print(rows)
            a=10
            subt=price
            n=2
            for row in rows:
                print(row)
                
                if row[0] in surg_list:
                    s="Surgery-",row[0]
                    no=tkinter.Label(frame1, text=n,font=("Arial",12,"bold"), bg="light gray")
                    n=n+1
                    subt+=int(row[1])

                    surgl=tkinter.Label(frame1, text=s,font=("Arial",12,"bold"),bg="light gray")
                    hyphen=tkinter.Label(frame1, text="--",font=("Arial",12,"bold"),bg="light gray")
                    cost=tkinter.Label(frame1, text=row[1],font=("Arial",12,"bold"), bg="light gray")
                    no.grid(row=a, column=0)                    
                    surgl.grid(row=a , column=1, stick=W, padx=5)
                    hyphen.grid(row=a , column=2)
                    cost.grid(row=a , column=3)
                    a=a+1

                elif row[0] in test_list:
                    t="Test-",row[0]
                    no=tkinter.Label(frame1, text=n,font=("Arial",12,"bold"), bg="light gray")
                    n=n+1
                    subt+=int(row[1])

                    testl=tkinter.Label(frame1, text=t,font=("Arial",12,"bold"), bg="light gray")
                    hyphen=tkinter.Label(frame1, text="--",font=("Arial",12,"bold"),bg="light gray")
                    cost=tkinter.Label(frame1, text=row[1],font=("Arial",12,"bold"),bg="light gray")
                    no.grid(row=a, column=0)
                    testl.grid(row=a , column=1, stick=W, padx=5)
                    hyphen.grid(row=a , column=2)
                    cost.grid(row=a , column=3)
                    a=a+1

            def tot():
                final=tkinter.Label(frame1, text=subt, font=("Arial",16,"bold"), bg="light gray")
                final.grid(row=a, column=3)
                conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
                c=conn.cursor()
                bb1=pat_ID.get()
                bb2=pat_name
                bb3=date1
                bb4=pat_date
                bb5=cat_var.get()
                bb6=subt
                c.execute('INSERT into bill values ({},"{}","{}","{}","{}",{});'.format(bb1,bb2,bb3,bb4,bb5,bb6))
                conn.commit()
                conn.close()
                
                
            t_bt=tkinter.Button(frame1, text="SUBTOTAL", command=tot,font=("Arial",12,"bold"), fg="white", bg="#022B63")
            t_bt.grid(row=a, column=2)
            
            
        genbt=tkinter.Button(frame1, text="Generate Bill", command=gen_bt,font=("Arial",12,"bold"), fg="white", bg="#022B63")
        
        namel.grid(row=2,column=0, pady=5)
        name.grid(row=2,column=1, pady=5,padx=3)
        genderl.grid(row=3,column=0, pady=5)
        gender.grid(row=3,column=1, pady=5, padx=3)
        agel.grid(row=4,column=0, pady=5)
        age.grid(row=4,column=1, pady=5, padx=3)
        conl.grid(row=5,column=0, pady=5)
        con.grid(row=5,column=1, pady=5,padx=3)

        date_adl.grid(row=2, column=2, pady=5)
        date_ad.grid(row=2, column=3, padx=3, pady=5)
        date_disl.grid(row=3, column=2, pady=5)
        dt_bt.grid(row =3, column =3, padx=3,pady=5)
        catl.grid(row=4, column=2, pady=5)
        cat.grid(row =4, column =3, padx=3,pady=5)        
        ctl.grid(row=5, column=2, pady=5)
        ct.grid(row =5, column =3, padx=3,pady=5)
        deptl.grid(row=6, column=2, pady=5)
        dept.grid(row =6, column =3, padx=3,pady=5)
        genbt.grid(row=7, column=1, columnspan=2)



        
    id_bt=tkinter.Button(frame1, text="Confirm", command=details)

    b_head.grid(row=0, column=0, columnspan=4)
    id.grid(row=1,column=0, padx=2)
    pat_ID.grid(row=1,column=1, padx=2)
    id_bt.grid(row=1, column=2, padx=2)
    
    rootB.iconbitmap('logo.ico')
    rootB.geometry("1200x800+50+50")
    rootB.mainloop()
