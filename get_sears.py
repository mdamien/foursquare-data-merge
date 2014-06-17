"""
HOW TO GET ALL SEARS SHOPS
1) get all sears shops in a few region by querying like this:
http://api.developer.sears.com/v2.1/stores/storeInfo/Sears/json/zip/91042/?apikey=SgwGuLpPtoHR5T7RzX7Mvvd3eiaOiJyi&mileRadius=1000
2) merge these results with this script
"""

import json
import copy

def make_hash(o):
  if isinstance(o, (set, tuple, list)):
    return tuple([make_hash(e) for e in o])    
  elif not isinstance(o, dict):
    return hash(o)

  new_o = copy.deepcopy(o)
  for k, v in new_o.items():
    new_o[k] = make_hash(v)

  return hash(tuple(frozenset(sorted(new_o.items()))))


if __name__ == '__main__':
    stores = []
    hashes = set()
    for zone in 'ny', 'cal', 'texas':
        raw = json.load(open('data/sears_{}.json'.format(zone)))
        arr = raw['showstoreinfo']['getstoreInfo']['Stores']['storelocation']
        print(zone, len(arr))
        for el in arr:
            h = make_hash(el)
            if h not in hashes:
                stores.append(el)
                hashes.add(h)       

    print('total',len(stores))
    with open('data/sears.json', 'w') as f:
        json.dump(stores, f)

