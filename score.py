"""
SCORE THE FUZZY DIFF BETWEEN THE ADDRESS
- use most_common to remove common words

Optional extra argument to filter the output:
ex:python2 score.py "score != 100 and score != 0 and score < 40" #low scores
"""
from __future__ import print_function
import json
from fuzzywuzzy import fuzz
import sys

combined = json.load(open('data/combined.json'))
common = set([l.strip() for l in open('data/most_common')])

def remove_common(adr):
    for c in '.#,':
        adr = adr.replace(c,'')
    return ' '.join(sorted(list(set(adr.split()) - common)))

c_0 = 0
c_100 = 0
c_sup_50 = 0
c_inf_50 = 0

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
    elif score > 50:
        color = '\033[94m'
        c_sup_50 += 1
    else:
        c_inf_50 += 1
    if len(sys.argv) == 1 or eval(sys.argv[1]):
        print(color,str(score).rjust(4), '|', address1.rjust(32), '|', address2+'\033[0m')

json.dump(combined, open('data/scored.json','w'), indent=2)

print()
print('STATS')
print('s == 0   [no address on fsq]:', c_0)
print('s == 100 [correct address on fsq]:', c_100)
print('s < 50 [ big diff ] :', c_inf_50)
print('s > 50 [ med to small diff ] :', c_sup_50)
