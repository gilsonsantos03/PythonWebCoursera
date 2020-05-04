import re

hand = open('exemplo.txt')
soma = 0

for line in hand:
    line = line.rstrip()
    resp = re.findall('[0-9]+', line)
    if len(resp) != 0:
        for i in resp:
            ##print(i)
            soma += int(i)

print(soma)