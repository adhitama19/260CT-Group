from tkinter import *
import os
import sqlite3
import sys



def deleteId():
    global staffIdE
    global nameE
    global surenameE
    global positionE
    global roots

    roots=Tk()
    roots.title('Remove An Account Menu')
    subTitle= Label(roots, text='Please enter the staff details below')
    subTitle.grid(row=0, column=0, sticky=E)
    
######################### THE LABELS ###########################################
    staffIdL= Label(roots,text='Enter staff ID: ')
    nameL= Label(roots,text='Enter Forename: ')
    surenameL= Label(roots,text='Enter Surename: ')
    positionL= Label(roots,text='Enter Position: ')
    staffIdL.grid(row=1, column=0, sticky=W)
    nameL.grid(row=2, column=0, sticky=W)
    surenameL.grid(row=3, column=0, sticky=W)
    positionL.grid(row=4, column=0, sticky=W)
    
######################### THE BOXES #############################################
    staffIdE= Entry(roots)    
    nameE= Entry(roots)
    surenameE= Entry(roots, show='*')
    positionE= Entry(roots)
    staffIdE.grid(row=1, column=1)
    nameE.grid(row=2, column=1)
    surenameE.grid(row=3, column=1)
    positionE.grid(row=4, column=1)
    
#########################  THE BUTTONS #############################################
    closeButton = Button(roots, text='Close', command=closeWindow) # CLOSE WINDOW
    closeButton.grid(row=5, column=0, sticky=W)
    removeButton = Button(roots, text='Remove staff?', command=checkIfdelete) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    removeButton.grid(row=5, column=1, sticky=W)
    roots.mainloop()

def closeWindow():
    roots.destroy()

    
def checkIfdelete():

    staffId= staffIdE.get()
    name= nameE.get()
    surename= surenameE.get()
    position= positionE.get()#GET INPUTS THATS TYPED IN BOXES
    
############### SQL DATABASE RETRIEVE AND DELETE ##################################
    connection = sqlite3.connect("Database.db")
    remove= connection.execute("DELETE FROM Manager_Login WHERE StaffID =? ", (staffId))#delete from the table 
    sql1= connection.execute("DELETE FROM Managers WHERE FORENAME = ? AND SURNAME = ? AND POSTION = ?",(staffId,name,surename,position))#deletes from the table 
    result=connection.execute("SELECT * FROM Managers, Manager_Login")#used to check if staff is still in the tables 
    connection.commit()
    print("row deleted: ", connection.total_changes)
        
    if staffId in result and username in result and surename in result and position in result:#checks if the staff have been removed.
        
        #see if input is correct
        r=Tk()
        r.geometry('160x65')
        rlbl=Label(r,text='the staff has not been deleted')
        delete= Label(r,text=print("staff remove from table(: ", connection.total_changes))#this shows if the staff have been removed
        delete.pack()
        rlbl.pack()
        r.mainloop()
    else:
        r=Tk()
        r.geometry('160x65')
        rlbl=Label(r,text='staff has been deleted')
        rlbl.pack()
        r.mainloop()        

    connection.close()   
   
deleteId()

