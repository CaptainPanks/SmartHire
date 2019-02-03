import datetime
import pprint
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import time
import firebase_admin
import cv2, imutils
from PhotoPreProcess import PreProcessing
from PhotoToText import PhotoToText

SECRET = '1GJH9o2MKFQqQEHOcEJuFjQmKtgZkITkWQvcpqw0'
DSN = 'https://smarthire-13139.firebaseio.com'
EMAIL = 'davyroosevelt@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

def writeToDB(data):
#    firebase.get('/uploads', None, params={'print': 'pretty'}, headers={'X_FANCY_HEADER': 'very fancy'})
    snapshot = firebase.post('/uploads', data)
    pprint.pprint(snapshot)



while True:
    image = cv2.imread("test.jpg")
    PreProcessing()
    data = PhotoToText()
    writeToDB(data)
    time.sleep(1)
    break
    
