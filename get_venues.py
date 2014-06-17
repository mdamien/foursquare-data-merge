"""
GET ALL SEARS SHOPS IN FOURSQUARE
- by querying randomly around sears shops
"""

import json
import math
import fsq
import random
import time
import merge_sears


stores = json.load(open('data/sears.json'))

all_venues = []
hashes = set()

while True:
    seed = random.choice(stores)
    blat = float(seed['location']['latitude'])
    blng = float(seed['location']['longitude'])
    
    print('seed:', blat,blng)
    venues = fsq.search(blat,blng)
    print('result:', len(venues))
    
    for el in venues:
        h = merge_sears.make_hash(el)
        if h not in hashes:
            all_venues.append(el)
            hashes.add(h)       
    print('total venues:', len(all_venues))
    with open('data/venues_tmp.json', 'w') as f:
        json.dump(all_venues, f)
    time.sleep(2)

