import json
import math
import random
import time

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

stores = json.load(open('data/sears.json'))
venues = json.load(open('data/venues.json'))

combined = []

for venue in venues:
    lat = venue['location']['lat']
    lng = venue['location']['lng']

    nearest = None
    min_d = None
    for store in stores:
        lat2 = float(store['location']['latitude'])
        lng2 = float(store['location']['longitude'])
        d = distance((lat,lng), (lat2,lng2))
        if not min_d or min_d > d:
            nearest = store 
            min_d = d

    if min_d < 0.2: #200 meters 
        combined += [{'venue': venue, 'store': nearest}]
        if len(combined) % 20 == 0:
            print(len(combined))
        with open('data/combined_tmp.json', 'w') as f:
            json.dump(combined, f, indent=4)
