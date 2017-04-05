import sys
import sqlite3 as sql
from random import randint
from tkinter import *

def ManagerAdd():
        global IDb
        global forenameB
        global surnameB
        global positionB
        global sqliteFile
        sqliteFile = 'Database.db'
        roots =Tk()
        roots.title('Add staff')

        Title1 = Label(roots, text='Please enter new staff details:')
        Title1.grid(row=0, column=0, sticky=E)

        forename = Label(roots,text='Enter Forename: ')
        surname = Label(roots,text='Enter Surename: ')
        position = Label(roots,text='Enter Position: ')

        forename.grid(row=1, column=0, sticky=W)
        surname.grid(row=2, column=0, sticky=W)
        position.grid(row=3, column=0, sticky=W)

        surnameB = Entry(roots)    
        forenameB = Entry(roots)
        select = StringVar(roots)
        select.set("Manager")
        positionB = OptionMenu(roots, select, "Manager","Instructor","Slope Operator")

        forenameB.grid(row=1, column=1)
        surnameB.grid(row=2, column=1)
        positionB.grid(row=3, column=1)

        Add = Button(roots, text='Add to database', command=AddF)
        Add.grid(row=5, column=0, sticky=W)
        roots.mainloop()
def AddF():
        Input = randint(0,9999)
        userInput2 = forenameB.get()
        userInput3 = surnameB.get()
        userInput4 = select.get()
        try:
                con = sql.connect(sqliteFile)
                cur = con.cursor()
                person = [(Input, userInput2, userInput3, userInput4)]
                cur.executemany('''INSERT INTO Managers (StaffID, Forename, Surname, Position) VALUES (?,?,?,?)''', person)
                con.commit()

        finally:
                con.close()

