'''
Sphere Booking and Check-in
260CT
prototype
Python 3
'''
from tkinter import *
import sqlite3
import string
import random
import sys
from random import randint

from removecustomer import *
from registration import *
from ManagerUpdating import *
from SkiInstructorTimetable import *
from SkiSlopeTimetable import *
from managerAdding import *
from member import *
from booking import *
from TimeTable import *
from home import *
             
def main():
    
    root=Tk()
    home=Home(root)
    root.mainloop()

if __name__ == '__main__':
    main()
        
        
