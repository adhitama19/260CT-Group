import sqlite3
import sys

def Maketimetable(date):
    eightam= str(None)
    tenam= str(None)
    twelvepm= str(None)
    twopm= str(None)
    fourpm= str(None)
    sixpm= str(None)

    conn= sqlite3.connect("Database.db") 
    c= conn.cursor()

    part1=str("Select customerID,session FROM Booking WHERE date = '")
    part2= str("' and time= '8:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    eightam= c.fetchone()
    eightam= str(eightam)

    part2= str("' and time= '10:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    tenam= c.fetchone()
    tenam= str(tenam) 

    part2= str("' and time= '12:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    twelvepm= c.fetchone()
    twelvepm= str(twelvepm)

    part2= str("' and time= '14:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    twopm= c.fetchone()
    twopm= str(twopm)

    part2= str("' and time= '16:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    fourpm= c.fetchone()
    fourpm= str(fourpm)

    part2= str("' and time= '18:00'")
    exe= str(part1+date+part2)
    c.execute(exe)
    sixpm= c.fetchone()
    sixpm= str(sixpm) 
    
    result=("8am:"+ eightam+ "\n"+ "10am:"+ tenam+ "\n"+ "12pm:"+ twelvepm+ "\n"+ "2pm:"+ twopm+ "\n"+ "4pm:"+ fourpm+ "\n"+ "6pm:"+ sixpm+ "\n")
    return(result) 
Test= Maketimetable("1/1/2018") 
print(Test) 
