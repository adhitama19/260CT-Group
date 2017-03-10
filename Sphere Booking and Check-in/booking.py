'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from Main import *

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
        
        self.c.execute("UPDATE Customer_details SET number_of_session = (?) WHERE ID = (?) ",
                       (sessionNumber, customerID))
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

        print(self.price)

        self.id_generator()
        
            
    def checkValue(self):

        firstName = self.firstName.get()
        surname = self.surname.get()
        dob = self.dob.get()
        
        self.c.execute("SELECT ID FROM Customer_Details WHERE FORENAME = ? AND SURNAME = ? AND DOB = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        self.customer = str(self.ID[0])

        self.c.execute("SELECT number_of_session FROM Customer_Details WHERE FORENAME = (?) AND SURNAME = (?) AND DOB = (?)",
                       (firstName, surname, dob))

        session = self.c.fetchone()
        self.sessionNum = int(session[0])
        self.sessionNum +=1
        print(self.sessionNum)
        
        self.calculate()  
    
