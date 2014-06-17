import json

from collections import Counter

combined = json.load(open('data/combined.json'))
counter = Counter()
for el in combined:
    store = el['store']
    venue = el['venue']
    for address in venue['location'].get('address'), store['location']['address']['streetaddress']:
        if address:
            counter.update(address.upper().split())

for word, n in counter.most_common(100):
    print(word)

