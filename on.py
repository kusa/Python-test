#!/usr/bin/python3

n = ("ahoj", 2, 45 , "pes", 84, "ahoj")
print(n.index("ahoj"))

print(n.count(2))

b = ["ahoj", 2, 45 , "pes", 84, "ahoj"]
b += ["vasek"];
c = ["ahoj", 2, 45 , "pes", 84, "ahoj", "vasek"]


d = [[1,2],[2,3]]
print('Delka', len(d))
for x,y in d:
    print(x,y)
    
import collections   
user = collections.namedtuple('user' , 'name passw gender')

co = user('Jan',1234,'male')
print(co._asdict())

se = [1,2,3,4,5]


jm = 'Moje jmeno je Ondra Tyrychtr'

a, *b, c = jm.split()



he = [1,2,3,4,5]

for i in range(len(he)):
    print(he[i])
    
leps = [z for z in range(10,20) if z % 2 == 0]

print(leps)
