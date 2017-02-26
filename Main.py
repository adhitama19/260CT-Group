from tkinter import *

class Login():

    def __init__(self,master):

        self.master= master
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

        self.label1.pack(side="top",padx=15,pady=15)
        
        self.label2.pack(side="top",padx=15,pady=15)
        self.input1.pack(side="top",padx=15,pady=15)
        
        self.label3.pack(side="top",padx=15,pady=15)
        self.input2.pack(side="top",padx=15,pady=15)
        self.button1.pack(side="top", padx=15,pady=15)
        
        # padx = horizonta
        # pady = verticle
        # .grid(row=6, column=2)
        # row = increase the number you move down, decrease the number  you move up.
        # column = increase the number you move right, decrease the number you move left.
    
        
    def check(self):
        
        root2=Toplevel(self.master)
        self.master.withdraw() # windows becomes invisible
        myGUI=Home(root2)

class Home():

    def __init__(self,master):
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

        self.button1=Button(self.master,text="Register new customer",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button2=Button(self.master,text="Upgrade member",fg="black", width=20, command=self.updateMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button3=Button(self.master,text="Register member",fg="black", width=20, command=self.regMember, height=3,font=("Helvetica",15, "bold italic"))
        self.button4=Button(self.master,text="Make new booking",fg="black", width=20, command=self.gotoBooking, height=3,font=("Helvetica",15, "bold italic"))
        self.button5=Button(self.master,text="Check booking",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button6=Button(self.master,text="Admin",fg="black", width=20,height=3,font=("Helvetica",15, "bold italic"))
        # Each button links to our individual function
        
        self.label1.pack(side="top",padx=15,pady=15)
        self.button1.pack(side="top",padx=15,pady=15)
        self.button2.pack(side="top",padx=15,pady=15)
        self.button3.pack(side="top",padx=15,pady=15)
        self.button4.pack(side="top",padx=15,pady=15)
        self.button5.pack(side="top",padx=15,pady=15)

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
        
    # Each function will execute the command to go to that specific window
        
class updateMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="Customer ID").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="First Name").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Surname").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Date of birth").grid(row=8)
        Label(self.master, text="    ").grid(row=9)
        Label(self.master, text="Type").grid(row=10)

        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)
        self.e4 = Entry(self.master)
        self.e5 = Entry(self.master)


        self.e1.grid(row=2, column=1)
        self.e2.grid(row=4, column=1)
        self.e3.grid(row=6, column=1)
        self.e4.grid(row=8, column=1)
        self.e5.grid(row=10, column=1)


        Button(self.master, text='Update',font=("Helvetica",15, "bold italic")).grid(row=11, column=2, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=2, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window


class regMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="Customer ID").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="First Name").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Surname").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Date of birth").grid(row=8)
        Label(self.master, text="    ").grid(row=9)
        Label(self.master, text="Phone number").grid(row=10)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="Date").grid(row=2,column=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Time").grid(row=4 ,column=2)

        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)
        self.e4 = Entry(self.master)
        self.e5 = Entry(self.master)
        self.e6 = Entry(self.master)
        self.e7 = Entry(self.master)


        self.e1.grid(row=2, column=1)
        self.e2.grid(row=4, column=1)
        self.e3.grid(row=6, column=1)
        self.e4.grid(row=8, column=1)
        self.e5.grid(row=10, column=1)
        self.e6.grid(row=2, column=3)
        self.e7.grid(row=4, column=3)


        Button(self.master, text='Create membership',font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window


 
class Booking():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
     
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="Customer ID").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="First Name").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Surname").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Date of birth").grid(row=8)
        Label(self.master, text="    ").grid(row=9)
        Label(self.master, text="Phone number").grid(row=10)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="Date").grid(row=2,column=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Time").grid(row=4 ,column=2)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Session").grid(row=6, column=2)

        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)
        self.e4 = Entry(self.master)
        self.e5 = Entry(self.master)
        self.e6 = Entry(self.master)
        self.e7 = Entry(self.master)
        self.e8 = Entry(self.master)


        self.e1.grid(row=2, column=1)
        self.e2.grid(row=4, column=1)
        self.e3.grid(row=6, column=1)
        self.e4.grid(row=8, column=1)
        self.e5.grid(row=10, column=1)
        self.e6.grid(row=2, column=3)
        self.e7.grid(row=4, column=3)
        self.e8.grid(row=6, column=3)


        Button(self.master, text='Book',font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window
        
def main():
    
    root=Tk()
    login=Login(root)
    root.mainloop()

if __name__ == '__main__':
    main()
        
        
