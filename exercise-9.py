import urllib2
import json

while True:
    keywords = raw_input("Keywords: ")
    if (keywords):
        break

keywords = " ".join(keywords.replace(",", " ").split())
keywords = urllib2.quote(keywords)

key = ''

response = urllib2.urlopen('http://api.brewerydb.com/v2/search?key=%s&q=%s&type=beer' % (key, keywords))
html = response.read()
beers = json.loads(html)

if 'data' in beers:
    beer = beers["data"][0]

    if 'name' in beer:
        print "Name: " + unicode(beer["name"].encode('UTF-8'), errors = 'ignore')

    if 'style' in beer and 'description' in beer["style"]:
        print "Description: " + beer["style"]["description"]

    if 'servingTemperatureDisplay' in beer:
        print "Serving Temperature: " + beer["servingTemperatureDisplay"]

    if 'available' in beer and 'name' in beer["available"]:
        print "Availability: " + beer["available"]["name"]
else:
    print "No results."
