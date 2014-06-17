from __future__ import print_function
import json
from fuzzywuzzy import fuzz

combined = json.load(open('data/combined.json'))
common = set([l.strip() for l in open('data/most_common')])

def remove_common(adr):
    return ' '.join(sorted(list(set(adr.split()) - common)))

c_0 = 0
c_100 = 0
c_other = 0

for el in combined:
    store = el['store']
    venue = el['venue']
    address_s = venue['location'].get('address','')
    address_f = store['location']['address']['streetaddress']
    address1 = remove_common(address_s.upper())
    address2 = remove_common(address_f.upper())
    score = fuzz.token_set_ratio(address1, address2)
    el['analysis'] = {'score':score, 'fq_address':address_s, 'sears_address':address_f}
    color = '\033[93m'
    if score == 0:
        color = '\033[91m'
        c_0 += 1
    elif score == 100:
        color = '\033[92m'
        c_100 += 1
    else:
        c_other += 1
    print(color,str(score).rjust(4), '|', address1.rjust(32), '|', address2+'\033[0m')

json.dump(combined, open('data/scored.json','w'), indent=2)

print()
print('stats:')
print('c(0) [no address on fsq]:', c_0)
print('c(100) [correct address on fsq]:', c_100)
print('others [ wrong address or small difference ] :', c_other)
