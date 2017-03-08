'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from tkinter import *
import sqlite3
import string
import random
import sys
from random import randint

from removecustomer import *
from registration import *
from ManagerUpdating import *
from SkiInstructorTimetable import *
from SkiSlopeTimetable import *
from managerAdding import *


class Home():

    def __init__(self,master):
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

        self.button1=Button(self.master,text="Register new customer",fg="black", width=20, command=self.register, height=3,font=("Helvetica",15, "bold italic"))
        self.button2=Button(self.master,text="Upgrade member",fg="black", width=20, command=self.updateMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button3=Button(self.master,text="Register member",fg="black", width=20, command=self.regMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button4=Button(self.master,text="Make new booking",fg="black", width=20, command=self.gotoBooking, height=3,font=("Helvetica",15, "bold italic"))
        self.button5=Button(self.master,text="Check booking",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button6=Button(self.master,text="time table",fg="black", width=20,command=self.table, height=3,font=("Helvetica",15, "bold italic"))
        self.button7=Button(self.master,text="Admin",fg="black", width=20, command=self.admin, height=3,font=("Helvetica",15, "bold italic"))
        # Each button links to our individual function
        
        self.label1.pack(side="top",padx=15,pady=15)
        self.button1.pack(side="top",padx=15,pady=15)
        self.button2.pack(side="top",padx=15,pady=15)
        self.button3.pack(side="top",padx=15,pady=15)
        self.button4.pack(side="top",padx=15,pady=15)
        self.button5.pack(side="top",padx=15,pady=15)
        self.button6.pack(side="top",padx=15,pady=15)
        self.button7.pack(side="top",padx=15,pady=15)

        # padx = horizonta
        # pady = verticle
        # .grid(row=6, column=2)
        # row = increase the number you move down, decrease the number  you move up.
        # column = increase the number you move right, decrease the number you move left.

    def gotoBooking(self):

        root3=Toplevel(self.master)
        self.master.withdraw()
        booking=Booking(root3,self.master)
        
    def updateMember(self):

        root4=Toplevel(self.master)
        self.master.withdraw()
        updatemember=updateMember(root4,self.master)
        
    def regMember(self):

        root5=Toplevel(self.master)
        self.master.withdraw()
        regmember=regMember(root5,self.master)

    def admin(self):

        root6=Toplevel(self.master)
        self.master.withdraw()
        adminlogin=adminLogin(root6,self.master)

    def register(self):
        
        self.master.withdraw()
        run()

    def table(self):

        root7=Toplevel(self.master)
        self.master.withdraw()
        timetable=timeTable(root7,self.master)
        
        
    # Each function will execute the command to go to that specific window


class timeTable():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master

        self.master.geometry("600x500+200+200") # size of the window
        self.master.title("Sphere Booking and Check-in")
        
        self.master.date = StringVar()
        self.master.ID = StringVar()

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))
        
        self.label2=Label(self.master,text="date:",fg="black", font=("Helvetica",12, "bold italic"))
        self.label3=Label(self.master,text="Staff ID:",fg="black", font=("Helvetica",12, "bold italic"))

        self.input1=Entry(self.master, textvariable=self.master.date)
        self.input2=Entry(self.master, textvariable=self.master.ID)

        self.button1=Button(self.master,text="Slope",fg="black",width=10, height=1,command=self.slopeOp)
        self.button2=Button(self.master,text="instructor",fg="black",width=10, height=1,command=self.instruct)
        self.button3=Button(self.master,text="Home",fg="black",width=10, height=1,command=self.home)

        self.label1.pack(side="top",padx=15,pady=15)
        
        self.label2.pack(side="top",padx=15,pady=15)
        self.input1.pack(side="top",padx=15,pady=15)

        self.label3.pack(side="top",padx=15,pady=15)
        self.input2.pack(side="top",padx=15,pady=15)
        
        self.button1.pack(side="top", padx=15,pady=15)
        self.button2.pack(side="top", padx=15,pady=15)
        self.button3.pack(side="top", padx=15,pady=15)
        
        
    def home(self):
        
        root2=Toplevel(self.master)
        self.master.withdraw() # windows becomes invisible
        myGUI=Home(root2)

    def slopeOp(self):

        self.master.withdraw()
        date = self.input1.get()
        runSlope= Maketimetable(date)
        printTimeTable(runSlope)

    def instruct(self):

        self.master.withdraw()
        date = self.input1.get()
        iid = self.input2.get()
        runInstruct = MaketimetableI(date,iid)
        printTimeTable(runInstruct)
        

class adminLogin():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master

        self.master.geometry("1080x800+200+200") # size of the window
        self.master.title("Sphere Booking and Check-in")
        
        self.master.username = StringVar()
        self.master.password = StringVar()

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))
        
        self.label2=Label(self.master,text="Username:",fg="black", font=("Helvetica",12, "bold italic"))
        self.label3=Label(self.master,text="password:",fg="black", font=("Helvetica",12, "bold italic"))

        self.input1=Entry(self.master, textvariable=self.master.username)
        self.input2=Entry(self.master, textvariable=self.master.password)

        self.button1=Button(self.master,text="Login",fg="black",width=10, height=1,command=self.check)
        self.button2=Button(self.master,text="Home",fg="black",width=10, height=1,command=self.home)

        self.label1.pack(side="top",padx=15,pady=15)
        
        self.label2.pack(side="top",padx=15,pady=15)
        self.input1.pack(side="top",padx=15,pady=15)
        
        self.label3.pack(side="top",padx=15,pady=15)
        self.input2.pack(side="top",padx=15,pady=15)
        
        self.button1.pack(side="top", padx=15,pady=15)
        self.button2.pack(side="top", padx=15,pady=15)
        
        
    def home(self):
        
        root2=Toplevel(self.master)
        self.master.withdraw() # windows becomes invisible
        myGUI=Home(root2)

    def check(self):

        root3=Toplevel(self.master)
        self.master.withdraw()
        admin=Admin(root3,self.master)


class Admin():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

        self.button1=Button(self.master,text="Add",fg="black", width=20,command=self.Add, height=3,font=("Helvetica",15, "bold italic"))
        self.button2=Button(self.master,text="Delete",fg="black", width=20, command=self.Delete, height=3,font=("Helvetica",15, "bold italic"))
        self.button3=Button(self.master,text="Update",fg="black", width=20, command=self.Update, height=3,font=("Helvetica",15, "bold italic"))
        self.button4=Button(self.master,text="Home",fg="black", width=20, command=self.home, height=3,font=("Helvetica",15, "bold italic"))
        
        self.label1.pack(side="top",padx=15,pady=15)
        self.button1.pack(side="top",padx=15,pady=15)
        self.button2.pack(side="top",padx=15,pady=15)
        self.button3.pack(side="top",padx=15,pady=15)
        self.button4.pack(side="top",padx=15,pady=15)

    def Add(self):

        self.master.withdraw()
        ManagerAdd()
        
    def Delete(self):
        
        self.master.withdraw()
        deleteId()
        
    def Update(self):
        
        self.master.withdraw()
        runUpdate()
        
    def home(self):
        
        root2=Toplevel(self.master)
        self.master.withdraw() # windows becomes invisible
        myGUI=Home(root2)
        
class updateMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="First Name").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth").grid(row=6)
        Label(self.master, text="    ").grid(row=7)


        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)

        self.e1.grid(row=2, column=1)
        self.e2.grid(row=4, column=1)
        self.e3.grid(row=6, column=1)


        Button(self.master, text='Update', command=self.checkValue, font=("Helvetica",15, "bold italic")).grid(row=11, column=2, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=2, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window

    def closeDB(self):
        self.c.close()
        self.conn.close()

    def updateMember(self):
        customerID = self.customer
        sessionNum = self.sessionNum
        loyalty = "loyalty"

        if sessionNum > 10:
            self.c.execute("UPDATE Member SET Membership_Type = (?) WHERE Customer_ID = (?) ",
                       (loyalty, customerID))
            self.conn.commit()
            self.closeDB()
        else:
            print("user does not have more than 10 sessions")
            print(sessionNum)
            
        
    def checkValue(self):

        firstName = self.e1.get()
        surname = self.e2.get()
        dob = self.e3.get()
        
        self.c.execute("SELECT ID FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        self.customer = str(self.ID[0])

        self.c.execute("SELECT number_of_session FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))

        session = self.c.fetchone()
        self.sessionNum = int(session[0])
        
        self.updateMember()   
        

class regMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="First Name").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Date").grid(row=2,column=2)
        Label(self.master, text="    ").grid(row=3)

        self.MFname = Entry(self.master)
        self.MSname = Entry(self.master)
        self.Mdob = Entry(self.master)
        self.Mdate = Entry(self.master)

        self.MFname.grid(row=2, column=1)
        self.MSname.grid(row=4, column=1)
        self.Mdob.grid(row=6, column=1)
        self.Mdate.grid(row=2, column=3)

        Button(self.master, text='Create membership', command=self.checkValue, font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window

    def closeDB(self):
        self.c.close()
        self.conn.close()
        self.goHome()
        
    def insertMember(self):
        customerID = int(self.customerID)
        date = self.Mdate.get()
        membershipType = "standard"
        membership = self.memID  
        
        self.c.execute("INSERT INTO Member ( Membership_ID, Customer_ID, Membership_Type, Join_Date) VALUES (?, ?, ?, ?)",
                       (membership, customerID, membershipType, date,))
        self.conn.commit()

        self.closeDB()
        
    def randomMemberID(self):
        range_start = 10**(10-1)
        range_end = (10**10)-1
        self.memID = randint(range_start, range_end)
        
        self.insertMember()
        
    def checkValue(self):

        firstName = self.MFname.get()
        surname = self.MSname.get()
        dob = self.Mdob.get()
        
        self.c.execute("SELECT ID FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        
        self.customerID = self.ID[0]
        
        self.randomMemberID()  
    

 
class Booking():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master

        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="First Name").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Session").grid(row=2, column=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Date").grid(row=4,column=2)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Time").grid(row=6 ,column=2)
        Label(self.master, text="    ").grid(row=7)
        
        self.firstName = Entry(self.master)
        self.surname = Entry(self.master)
        self.dob = Entry(self.master)
        self.session = Entry(self.master)
        self.date = Entry(self.master)
        self.time = Entry(self.master)

        self.firstName.grid(row=2, column=1)
        self.surname.grid(row=4, column=1)
        self.dob.grid(row=6, column=1)
        self.session.grid(row=2, column=3)
        self.date.grid(row=4, column=3)
        self.time.grid(row=6, column=3)

        Button(self.master, text='Book', command=self.checkValue, font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Timetable', command=self.table, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=13, column=4, sticky=W, pady=4)


    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window
        
    def table(self):
        root1=Toplevel(self.master)
        timetable=timeTable(root1,self.master)

    def closeDB(self):
        self.c.close()
        self.conn.close()

    def insertBooking(self):
        refNum = self.ref
        customerID = self.customer
        session = self.session.get()
        date = self.date.get()
        time = self.time.get()
        checking = "False"
        price = self.price
        sessionNumber = self.sessionNum

        self.c.execute("INSERT INTO Booking (Ref_number, customerID, session, date, time, checking, price) VALUES(?, ?, ?, ?, ?, ?, ?)",
                       (refNum, customerID, session, date, time, checking, price))
        self.c.execute("INSERT INTO Customer_details (number_of_session) VALUES (?)",
                       (sessionNumber))
                           
        self.conn.commit()
        
        self.closeDB()

    def id_generator(self,size=16, chars=string.ascii_uppercase + string.digits):
        self.ref=''.join(random.choice(chars) for _ in range(size))
        self.insertBooking()

    def calculate(self):
        session = self.session.get()
        cID = self.customer
        
        normal = 50 # price per hour
        instructor = 20 #price per hour
        self.price = 0

        self.c.execute("SELECT Membership_Type FROM Member WHERE Customer_ID = ?",
                       (cID))
        
        self.status =self.c.fetchone()
        
        membershipType = self.status[0]

        if membershipType.lower() == "standard":
            if session.lower() == "normal":
                self.price = normal
            else:
                self.price = normal + instructor
        else:
            if session.lower() == "normal":
                discount = (normal * 20) / 100
                self.price = normal - discount
                
            else:
                discount = (normal + instructor * 20) / 100
                self.price = normal + instructor - discount

        self.id_generator()
        
            
    def checkValue(self):

        firstName = self.firstName.get()
        surname = self.surname.get()
        dob = self.dob.get()
        
        self.c.execute("SELECT ID FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        self.customer = str(self.ID[0])

        self.c.execute("SELECT number_of_session FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))

        session = self.c.fetchone()
        self.sessionNum = int(self.ID[0])
        self.sessionNum +=1
        
        self.calculate()  
    
        
         
def main():
    
    root=Tk()
    home=Home(root)
    root.mainloop()

if __name__ == '__main__':
    main()
        
        
