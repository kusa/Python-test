#!/usr/bin/python3.2

import collectxdsions 
import test1

a=1
dict = {'jmeno':'Ondra', 'Prijmeni': 'Borec', 'Age': 23}

del dict['Prijmeni']

for key,val in dict.items():
    print(key, ' - ', val)
    
li  =[1,2]
for v in li:
    print(v)