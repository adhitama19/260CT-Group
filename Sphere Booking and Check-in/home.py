'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from Main import *

class Home():

    def __init__(self,master):
        
        self.master= master
        self.master.geometry("1080x800")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

        self.button1=Button(self.master,text="Register new customer",fg="black", width=20, command=self.register, height=3,font=("Helvetica",15, "bold italic"))
        self.button2=Button(self.master,text="Upgrade member",fg="black", width=20, command=self.updateMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button3=Button(self.master,text="Register member",fg="black", width=20, command=self.regMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button4=Button(self.master,text="Make new booking",fg="black", width=20, command=self.gotoBooking, height=3,font=("Helvetica",15, "bold italic"))
        self.button5=Button(self.master,text="Check booking",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button6=Button(self.master,text="time table",fg="black", width=20,command=self.table, height=3,font=("Helvetica",15, "bold italic"))
        self.button7=Button(self.master,text="Admin",fg="black", width=20, command=self.adminCommand, height=3,font=("Helvetica",15, "bold italic"))
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

    def adminCommand(self):

        root6 = Toplevel(self.master)
        self.master.withdraw()
        adminCommand = Login(root6,self.master)

    def table(self):

        root7=Toplevel(self.master)
        self.master.withdraw()
        timetable=timeTable(root7,self.master)

    def register(self):
        
        self.master.withdraw()
        run()
        
    # Each of these functions are linked to each of our functionalities
    

class Login():

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

        # padx = horizonta
        # pady = verticle
        # .grid(row=6, column=2)
        # row = increase the number you move down, decrease the number  you move up.
        # column = increase the number you move right, decrease the number you move left.
        
    def home(self):

        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window

    def AdminGui(self):

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
        
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window
        


