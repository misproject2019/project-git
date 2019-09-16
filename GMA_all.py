import googlemaps
import time
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

gmaps = googlemaps.Client(key="AIzaSyCI3YcPn9vLcIJgIjSR51xzhD7Ghrar9zU ")

g = input("請輸入地址")
geocode_result = gmaps.geocode(g)

ids = []
results = []
loc = geocode_result[0]['geometry']['location']
query_result = gmaps.places_nearby(keyword = "日式", type = None,location = loc, radius = 2000)
results.extend(query_result['results'])

while query_result.get('next_page_token'):
    time.sleep(2)
    query_result = gmaps.places_nearby(page_token = query_result['next_page_token'])
    results.extend(query_result['results'])
for place in results:
    ids.append(place['place_id'])

stores_info = []
ids = list(set(ids))
for id in ids:
    stores_info.append(gmaps.place(place_id = id, language = "zh-TW")["result"])

for result in stores_info:
    print (result["name"])
    j = 6 
    restid = []
    restid = ''.join(str(i) for i in random.sample(range(1,9),j))
    phone = result['formatted_phone_number'] if 'formatted_phone_number' in result else None
    address = result['formatted_address'] if 'formatted_address' in result else None
    time = result['opening_hours']['weekday_text'] if 'opening_hours' in result else None
    rating = result['rating'] if 'rating' in result else None
    if 'photos' in result:
        photos = result['photos'][0]['photo_reference'] 
        p = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + photos +"&key=AIzaSyCI3YcPn9vLcIJgIjSR51xzhD7Ghrar9zU"
    else:
        p = None
    data = {"name":result['name'], "phone":phone, "address":address, "time":time ,"rating":rating, "photos":p}

    try:
        db.child("restaurant").order_by_child("name").equal_to("test").get()
    except IndexError:
        pass
    else:
        db.child("restaurant").child(restid).set(data)

'''
    res=db.child("restaurant").get()
    for restaurant in res.each():
        if result["name"] == db.child("restaurant").child(restaurant.key()).child("name").get().val():
            pass
        else:
            db.child("restaurant").child(restid).set(data)
            '''
    