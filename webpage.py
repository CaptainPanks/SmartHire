import time
import os

import datetime
import pprint
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import firebase_admin



SECRET = '1GJH9o2MKFQqQEHOcEJuFjQmKtgZkITkWQvcpqw0'
DSN = 'https://smarthire-13139.firebaseio.com'
EMAIL = 'davyroosevelt@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

def getList(keyword):
    result = firebase.get('/uploads', None)
    if result:
        pprint.pprint(result)
    else:
        print('Empty Set!')
        


while True:
    file = '/Applications/MAMP/htdocs/webpage/mydata.txt'
    if os.stat(file).st_size == 0: # the file is empty
        time.sleep(1)
    else:
        with open(file,'r') as f:
            data = f.read()
            getList(data)
            os.remove(file)
            open(file,'a').close()
