import re

string = 'oi eu sou o 1 goku e tambem O 3 goku'

y = re.findall('[aeiou]+',string)
z = re.findall('[0-9]+',string)
print(y)
print(z)

#############################################333

string2 = 'From: Using the : character'
y2 = re.findall('^F.+:', string2)
print(y2)
correct = re.findall('^F.+?:', string2)
print(correct)

################################################

string3 = 'From gilsonlopes1921@gmail.com sat jan 2102-09-21'
y3 = re.findall('\S+@\S+', string3)
print(y3)

y4 = re.findall('^From (\S+@\S+)', string3)
##os parenteses indicam onde comeca e onde deve parar a string a ser extraida
print(y4)

y5 = re.findall('@([^ ]*)', string3)
print(y5)
y5 = re.findall('^From .*@([^ ]*)', string3)

#####################################3

string5 = 'isso custou apenas $10.00 for cookies'

y43 = re.findall('\$[0-9.]+', string5)
print(y43)