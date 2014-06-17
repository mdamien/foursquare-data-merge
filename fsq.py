"""
BASIC FOURSQUARE API INTERACTION HELPERS
"""

import requests

SUFFIX = '?oauth_token=0Q235XWN4ACGAPLRUTRUGBQFV1HWN4RVXCMHVE0EAETX2DMC&v=20140607'
BASE = 'https://api.foursquare.com/v2/'

def url(endpoint, **kwargs):
    s = BASE+endpoint+SUFFIX
    for key in kwargs:
        s += '&'+key+'='+str(kwargs[key])
    return s

def search(lat,lng):
    resp = requests.get(url('venues/search', ll="%s,%s" % (lat, lng), query="Sears", limit=50))
    return resp.json()['response']['venues']

def propose_edit(venue_id, **payload):
    return requests.post(url('venues/%s/proposeedit' % venue_id), data=payload)

if __name__ == '__main__':
    from pprint import pprint as pp
    pp(search(40.7,-74))
