import tkinter as tk
import sys
import sqlite3

window = tk.Tk()
window.title('Please enter your reference number')
window.geometry('450x300')

tk.Label(window,text='search booking').place(x=50,y=120)

var_ref_num = tk.StringVar()
entry_ref_num = tk.Entry(window,textvariable=var_ref_num)
entry_ref_num.place(x=160,y=120)

def usr_enter():
   stringx = entry_ref_num.get() #x must be string or made into string at later point
   conn = sqlite3.connect('database.db')
   print ("Opened database successfully");

   executeme= str("UPDATE Booking set checking = 'True' where Ref_number = "+ stringx) 
   conn.execute(executeme)
   conn.commit()
   print ("Total number of rows updated :"), conn.total_changes

   cursor = conn.execute("SELECT * from Booking where Ref_number = "+stringx)
   for row in cursor:
      print ("Ref_number =  " + str(row[0]))
      print ("customerID = " + str(row[1]))
      print ("session = " + str(row[2]))
      print ("date = " + str(row[3]))
      print ("time = " + str(row[4]))
      print ("checking = "+ str(row[5]))
      print ("Instructor = "+ str(row[6]) +"\n")

   print ("Operation done successfully");
   conn.close()
def customer_enter():
   window_cus_enter = tk.Toplevel(window)
   window_cus_enter.geometry('450x300')
   window_cus_enter.title('please enter your customerID')

   tk.Label(window_cus_enter,text='search booking').place(x=50,y=120)

   var_cus_num = tk.StringVar()
   entry_cus_num = tk.Entry(window_cus_enter,textvariable=var_cus_num)
   entry_cus_num.place(x=160,y=120)

   btn_enter = tk.Button(window_cus_enter,text='enter',command=usr_enter)
   btn_enter.place(x=150, y=170)

   def id_enter():
      
      stringy = entry_ref_num.get() #y must be string or made into string at later point
      conn = sqlite3.connect('database.db')
      print ("Opened database successfully");

      executeme2= str("UPDATE Booking set checking = 'True' where customerID = "+ stringy) 
      conn.execute(executeme2)
      conn.commit()
      print ("Total number of rows updated :"), conn.total_changes

      cursor = conn.execute("SELECT * from Booking where customerID = "+stringy)
      for row in cursor:
         print ("Ref_number =  " + str(row[0]))
         print ("customerID = " + str(row[1]))
         print ("session = " + str(row[2]))
         print ("date = " + str(row[3]))
         print ("time = " + str(row[4]))
         print ("checking = "+ str(row[5]))
         print ("Instructor = "+ str(row[6]) +"\n")

         print ("Operation done successfully");
      conn.close()
   
btn_enter = tk.Button(window,text='enter',command=usr_enter)
btn_enter.place(x=150, y=170)
btn_customer = tk.Button(window,text='Use customerID for searching',command=customer_enter)
btn_customer.place(x=200, y=170)
window.mainloop()

