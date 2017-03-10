'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from Main import *

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
