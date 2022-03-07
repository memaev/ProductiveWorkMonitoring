import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import eel
from datetime import date
import os
from tkinter import *

cred = credentials.Certificate('firebase-admin.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://productivework-9ccd1-default-rtdb.firebaseio.com/'
})

def getDate():
    today = date.today()
    dt = today.strftime("%d/%m/%y")
    return dt

def getWorkingTime():
    ref = db.reference('/')
    working_time = ref.child('Users').child(os.getlogin()).child('working-time').get()
    if (working_time is None):
        return "No statistics yet"
    else:
        working_time = int(working_time)
        hrs = int(working_time)/3600
        hrs = int(hrs)
        working_time -= hrs*3600;
        mins = working_time/60;
        mins = int(mins)
        return str(hrs)+" hrs "+str(mins)+" mins today"

def getNotWorkingTime():
    ref = db.reference('/')
    working_time = ref.child('Users').child(os.getlogin()).child('not-working-time').get()
    if (working_time is None):
        return "No statistics yet"
    else:
        working_time = int(working_time)
        hrs = int(working_time)/3600
        hrs = int(hrs)
        working_time -= hrs*3600;
        mins = working_time/60;
        mins = int(mins)
        return str(hrs)+" hrs "+str(mins)+" mins today"

root = Tk()
date_txt = Label(root, text="Date: " + getDate())
working_time = Label(root, text="Work: " + getWorkingTime() + "  today")
not_working_time = Label(root, text="Rest : " + getNotWorkingTime() + " today")
login = Label(root, text="PC Login: " + os.getlogin())

login.grid(row=0, column=0)
date_txt.grid(row=1, column=0)
working_time.grid(row=2, column=0)
not_working_time.grid(row=3, column=0)


root.mainloop()
