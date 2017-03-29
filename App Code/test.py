import tkinter
import sqlite3
from tkinter import *
from tkinter import ttk


class App():

    def __init__ (self, master):

        frame = Frame(master)
        frame.pack()

        
        foreName = StringVar()
        surName = StringVar()
        doBirth = StringVar()
        accountStat = StringVar()
        numberSess = StringVar()
        balance = StringVar()

        
        foreName1 = StringVar()
        surName1 = StringVar()
        doBirth1 = StringVar()
        customerExp1 = StringVar()
        accountStat1 = StringVar()
        numberSess1 = StringVar()
        balance1 = StringVar()

        options = [ "Novice", "Member" ]

        self.conn = sqlite3.connect('Database.db')
        self.cur = self.conn.cursor()
        print('Database Opened Successfully')

        #GUI Button
        
        self.button2 = Button (frame, text = 'Insert Data', command = self.insertDb)
        self.button2.grid(row = 0, column = 1)

        #GUI Entry and Label for Insert

        self.l2 = Label(frame, text = "First Name")
        self.l2.grid(row = 3, column = 0)
        self.foreName = Entry(frame, bd = 6)
        self.foreName.grid(row = 3, column = 1)

        self.l3 = Label(frame, text = "Surname")
        self.l3.grid(row = 4, column = 0)
        self.surName = Entry(frame, bd = 7)
        self.surName.grid(row = 4, column = 1)

        self.l4 = Label(frame, text = "Date of Birth")
        self.l4.grid(row = 5, column = 0)
        self.doBirth = Entry(frame, bd = 8)
        self.doBirth.grid(row = 5, column = 1)

        self.l5 = Label(frame, text = "Customer Experience")
        self.l5.grid(row = 6, column = 0)
        self.customerExp = Radiobutton(frame, text="Novice", variable=customerExp1, value="Novice")
        self.customerExp1 = Radiobutton(frame, text="Members", variable=customerExp1, value="Member") 
        self.customerExp.grid(row = 6, column = 1)
        self.customerExp1.grid(row = 7, column = 1)
        

        self.l7 = Label(frame, text = "Number of Session")
        self.l7.grid(row = 8, column = 0)
        self.numberSess = Entry(frame, bd = 10)
        self.numberSess.grid(row = 8, column = 1)

        self.l8 = Label(frame, text = "Account Balance")
        self.l8.grid(row = 9, column = 0)
        self.balance = Entry(frame, bd = 11)
        self.balance.grid(row = 9, column = 1)


    def insertDb(self):
        
        
        foreName1 = self.foreName.get() 
        surName1 = self.surName.get()
        doBirth1 = self.doBirth.get()
        x = self.customerExp1.get()
        numberSess1 = int(self.numberSess.get())
        balance1 = int(self.balance.get())

        self.cur.execute("INSERT INTO Customer \
(CustomerID, FirstName, surname, date_of_birth, customer_experience, number_of_sessions, balance_owed)\
VALUES (NULL, ?, ?, ?, ?, ?, ?)", (foreName1, surName1, doBirth1, x,numberSess1, balance1))

        self.conn.commit()
        self.conn.close()
        print("Database is now Closed")



        

root = tkinter.Tk()
root.title("Sphere Registration Table")
root.geometry('700x400')

app = App(root)
root.mainloop()
