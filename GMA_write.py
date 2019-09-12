import googlemaps
import time
import json

gmaps = googlemaps.Client(key="AIzaSyCI3YcPn9vLcIJgIjSR51xzhD7Ghrar9zU ")

g = input("請輸入地址")
geocode_result = gmaps.geocode(g)

ids = []
results = []
loc = geocode_result[0]['geometry']['location']
query_result = gmaps.places_nearby(keyword = "咖啡店",location = loc, radius = 5000)
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
    name = result['name']
    file_name = name + ".json"
    if "/" in name:
        pass
    else:
        with open (file_name, "w") as file_object:
            json.dump(result, file_object)

    