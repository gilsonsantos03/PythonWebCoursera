# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

c = count
lista = []
while (c > 0):

    if (c == count):
        url = 'http://py4e-data.dr-chuck.net/known_by_Marin.html'
    else:
        url = lista[position - 1]
        lista.clear()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        formatado = tag.get('href', None)
        lista.append(formatado)
    
    print('Retrieving: ', lista[position - 1])
    c -= 1
