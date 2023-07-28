
from tkinter import*
from PIL import ImageTk
import tkinter.messagebox
import matplotlib.pyplot as plt
import pymysql
from h3_pat_form import PAT
from h4_pat_record import SUR_TEST
from h5_employee_reg import EMP
from h6_app_form import APP
from h7_bill import BILL


#EXIT for MENU
def gp():
    global root2
    conn=pymysql.connect(host="localhost", user="root", password="password", database="VTREAT")
    c=conn.cursor()
    c.execute("select age from PATIENT;")
    ages=c.fetchall()
    plt.hist(ages,bins=9)
    plt.title("Patient Age Histogram")
    plt.ylabel("Number of Patients in Hospital")
    plt.xlabel("Ages")
    plt.show()
    #root2.destroy()

#MENU BUTTONS
def menu():
    global root2,button1,button2,button3,button4,button5,m,button6
    class Login:
        def __init__(self,root2):
            self.root2=root2
            #BGimage
            self.bg=ImageTk.PhotoImage(file="hospital1.jpg")
            self.bg_image=Label(root2, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            frame=Frame(self.root2, bg='white',highlightbackground="light gray", highlightthickness=2).place(x=298, y=120, height=350, width=604)    
    root2=tkinter.Tk()
    Call=Login(root2)
    root2.title("MAIN MENU")
    m=tkinter.Label(root2,text="MENU",font='Goudyoldstyle 30 bold ',fg='#022B63',bg="white")
    button1=tkinter.Button(root2,text="PATIENT \n REGISTRATION",command=PAT,bg='light gray',fg='#022B63',font='Arial 12 bold',)#bd=0)
    button2 = tkinter.Button(root2, text="PATIENT \nRECORD",bg='#022B63',fg='light gray',command=SUR_TEST,font='Arial 12 bold',)#bd=0)
    button3 = tkinter.Button(root2, text="EMPLOYEE \n REGISTRATION",bg='light gray',fg='#022B63',command=EMP,font='Arial 12 bold',)#bd=0) 
    button4 = tkinter.Button(root2, text="BOOK APPOINTMENT\n  O.P.D.",bg='#022B63',fg='light gray',command=APP,font='Arial 12 bold',)#bd=0)
    button5 = tkinter.Button(root2, text="PATIENT BILL",bg='light gray',fg='#022B63',command=BILL,font='Arial 12 bold',)#bd=0)
    button6 = tkinter.Button(root2, text="AGE GRAPH",command=gp,bg='#022B63',fg='light gray',font='Arial 12 bold',)#bd=0)
    m.place(x=535,y=120)

    button1.place(x=300,y=170, width=198, height=148)

    button2.place(x=500,y=170, width=198, height=148)
    
    button3.place(x=700,y=170, width=198, height=148)

    button4.place(x=300, y=320, width=198, height=148)

    button5.place(x=500,y=320, width=198, height=148)

    button6.place(x=700,y=320, width=198, height=148)

    
    root2.iconbitmap('logo.ico')
    root2.geometry("1199x600+100+50")
    root2.resizable(False,False)
    
    root2.mainloop()



