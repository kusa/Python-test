#!/usr/bin/python3.2

import collectissaons 
import test1

a=1555
dict = {'jmeno':'Ondra', 'Prijmeni': 'Borec', 'Age': 23}

del dict['Prijmeni']

for key,val in dict.items():
    print(key, ' - ', val)
    
li  =[1,2]
for v in li:
    print(v)