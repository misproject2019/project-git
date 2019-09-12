import json
import pyrebase
import random
import os

config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
 
path = r"C:\Users\Regina\Desktop\專題\restaurant\google map"
files = os.listdir(path)
s = []
for file in files:
    if "json" in file :
        with open(file, 'r') as reader:
            js = json.loads(reader.read())
            j = 6 
            restid = []
            restid = ''.join(str(i) for i in random.sample(range(0,9),j))
            phone = js['formatted_phone_number'] if 'formatted_phone_number' in js else None
            address = js['formatted_address'] if 'formatted_address' in js else None
            time = js['opening_hours']['weekday_text'] if 'opening_hours' in js else None
            rating = js['rating'] if 'rating' in js else None
            if 'photos' in js:
                photos = js['photos'][0]['photo_reference'] 
                p = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + photos +"&key=AIzaSyCI3YcPn9vLcIJgIjSR51xzhD7Ghrar9zU"
            else:
                p = None
            data = {"name":js['name'], "phone":phone, "address":address, "time":time ,"rating":rating, "photos":p}

            res=db.child("restaurant").get()
            for restaurant in res.each():
                if js["name"] == db.child("restaurant").child(restaurant.key()).child("name").get().val():
                    db.child("restaurant").child(restid).update(data)
                else:
                    db.child("restaurant").child(restid).set(data)






