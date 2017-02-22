import sqlite3
import sys

def Maketimetable(Date):
    date=(str(Date)) 
    eightam= None
    tenam= None
    twelvepm= None
    twopm= None
    fourpm= None
    sixpm= None

    conn= sqlite3.connect("Database.db") 
    c= conn.cursor()


    exe= str("Select customerID,session FROM Booking WHERE date = '1/1/2018' and time= '8:00'")
    c.execute(exe)
    eightam= c.fetchone()

    
    print(" 8am:", eightam, "\n", "10am:", tenam, "\n", "12pm:", twelvepm, "\n", "2pm:", twopm, "\n", "4pm:", fourpm, "\n", "6pm:", sixpm, "\n")

Maketimetable(1/1/2018) 
