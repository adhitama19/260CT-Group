from tkinter import *

class Login():

    def __init__(self,master):

        self.master= master
        self.master.geometry("1080x800+200+200")
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
    
        
    def check(self):

        root2=Toplevel(self.master)
        myGUI=Home(root2)

class Home():

    def __init__(self,master):
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

        self.button1=Button(self.master,text="Register new customer",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button2=Button(self.master,text="Register/Upgrade member",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button3=Button(self.master,text="Make new booking",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button4=Button(self.master,text="Check booking",fg="black", width=20, height=3,font=("Helvetica",15, "bold italic"))
        self.button5=Button(self.master,text="Admin",fg="black", width=20,height=3,font=("Helvetica",15, "bold italic"))
        # Each button will link to our individual work
        
        

        self.label1.pack(side="top",padx=15,pady=15)
        self.button1.pack(side="top",padx=15,pady=15)
        self.button2.pack(side="top",padx=15,pady=15)
        self.button3.pack(side="top",padx=15,pady=15)
        self.button4.pack(side="top",padx=15,pady=15)
        self.button5.pack(side="top",padx=15,pady=15)
        
class Booking():

    def __init__(self,master):
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))

def main():
    
    root=Tk()
    myGUIWelcome=Login(root)
    root.mainloop()

if __name__ == '__main__':
    main()
        
        
