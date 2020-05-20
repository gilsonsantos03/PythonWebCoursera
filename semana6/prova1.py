import json
import urllib.request

url_input = input('URL:')
uh = urllib.request.urlopen(url_input)
data = uh.read()

print('Retrieved', len(data), 'characters')

info = json.loads(data)

count = info["comments"]
print('Count:', len(count))

sum = 0
c = 0
for i in count:
    sum += i["count"]
    c += 1
print('Sum:', sum)