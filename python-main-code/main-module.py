import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import apps_checking
from datetime import date

cap = cv2.VideoCapture(1)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change
is_here = 0

cred = credentials.Certificate('firebase-admin.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://productivework-9ccd1-default-rtdb.firebaseio.com/'
})


ref = db.reference('/')
curtime = 0

def increment():
    ref = db.reference('/')
    #working_time = ref.child('Users').child(os.getlogin()).child('working-time').get()
    last_update = ref.child('Users').child(os.getlogin()).child('last-update').get()
    today = date.today()
    dt = today.strftime("%d/%m/%y")
    if last_update is None:
        last_update = dt
        ref.child('Users').child(os.getlogin()).set({
            'working-time': 30,
            'last-update': dt,
            'not-working-time': 0
        })
    else:
        if (last_update!=dt):
            not_working_time = ref.child('Users').child(os.getlogin()).child('not-working-time').get()
            working_time = ref.child('Users').child(os.getlogin()).child('working-time').get()
            if (not_working_time is None):
                not_working_time = 0
            if (working_time is None):
                working_time = 0
            ref.child('Users').child(os.getlogin()).child(last_update).set({
                'not-working-time': not_working_time, 
                'working-time': working_time
            })
            ref.child('Users').child(os.getlogin()).update({
                'not-working-time': 0, 
                'working-time': 30, 
                'last-update': dt
            })
        else:
            working_time=ref.child('Users').child(os.getlogin()).child('working-time').get()
            if working_time is None:
                working_time=30
            else:
                working_time+=30
            ref.child('Users').child(os.getlogin()).update({
                'working-time':working_time, 
                'last-update':dt
            })


def decrement():
    ref = db.reference('/')
    last_update = ref.child('Users').child(os.getlogin()).child('last-update').get()
    today = date.today()
    dt = today.strftime("%d/%m/%y")
    if last_update is None:
        last_update = dt
        ref.child('Users').child(os.getlogin()).set({
            'working-time': 0,
            'last-update': dt,
            'not-working-time': 30
        })
    else:
        if (last_update!=dt):
            not_working_time = ref.child('Users').child(os.getlogin()).child('not-working-time').get()
            working_time = ref.child('Users').child(os.getlogin()).child('working-time').get()
            if (not_working_time is None):
                not_working_time = 0
            if (working_time is None):
                working_time = 0
            ref.child('Users').child(os.getlogin()).child(last_update).set({
                'not-working-time': not_working_time, 
                'working-time': working_time
            })
            ref.child('Users').child(os.getlogin()).update({
                'not-working-time': 30, 
                'working-time': 0, 
                'last-update': dt
            })
        else:
            not_working_time=ref.child('Users').child(os.getlogin()).child('not-working-time').get()
            if not_working_time is None:
                not_working_time=30
            else:
                not_working_time+=30
            ref.child('Users').child(os.getlogin()).update({
                'not-working-time': not_working_time, 
                'last-update':dt
            })

while (1):
    ret, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    is_here = 0
    for x, y, w, h in faces:
        is_here = 1
        if (apps_checking.check()):
            increment()
        else:
            decrement()
    if (is_here==0):
        decrement()
    
    cv2.waitKey(30000)
