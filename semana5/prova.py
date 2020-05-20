import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_input = input('URL:')
uh = urllib.request.urlopen(url_input)
data = uh.read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

contadores = tree.findall('.//comment')
print('Count:', len(contadores))

counts = tree.findall('comments/comment')

soma = 0
for c in counts:
    soma += int(c.find('count').text)

print('Soma: ', soma)