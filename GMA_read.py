import json
import pyrebase
import random

config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

with open('LALA Kitchen 新美式餐廳.json', 'r') as reader:
    js = json.loads(reader.read())

    j = 6 
    restid = []
    restid = ''.join(str(i) for i in random.sample(range(0,9),j))
    data = {"name":js['name'], "phone":js['formatted_phone_number'], "address":js['formatted_address'], "time":js['opening_hours']['weekday_text']}
    db.child("restaurant").child(restid).set(data)





