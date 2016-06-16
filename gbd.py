# -*- coding: utf-8 -*-
import json
from geopy.distance import vincenty
from geopy.distance import great_circle
import operator
import optparse

parser = optparse.OptionParser()
parser.add_option('-l', '--loc', dest='basecoord', help='Current location like (53.3381985, -6.2592576)', default=(53.3381985, -6.2592576))
parser.add_option('-p', '--place', dest='baseplace', help='Current place like Dublin', default='')
parser.add_option('-d', '--dist', dest='dist', help='Needed distance', default=100)
parser.add_option('-f', '--file', dest='file', help='Input file with customers list', default='customers.txt')
parser.add_option('-t', '--type', dest='type', help='Type of calc: vincenty(1) or great_circle(2)', default=1)
options, args = parser.parse_args()

if options.baseplace:
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    location = geolocator.geocode(options.baseplace)
    options.basecoord = (location.latitude, location.longitude)

jsonFile = open(options.file, 'r')

values = {'customers':[]}
#values = json.load(jsonFile)
for line in jsonFile:
    tmp = json.loads(line)
    values['customers'].append(tmp)
    
res = []
for v in values['customers']:
    if options.type == 1:
        dist = round(vincenty(options.basecoord, (v[u'latitude'], v[u'longitude'])).km, 2)
    else:
        dist = round(great_circle(options.basecoord, (v[u'latitude'], v[u'longitude'])).km, 2)
    
    if dist <= float(options.dist):
        del v[u'latitude']
        del v[u'longitude']
        v.update({'dist':dist})
        res.append(v)

sortres = sorted(res, key=lambda k: k['user_id'])

[dict(s).pop(u'latitude', None) for s in sortres]
print len(sortres)
out = open('res.json','w+b')
out.write(json.dumps(sortres))
out.close()
