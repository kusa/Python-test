#!/usr/bin/python3.2

import collections

dict = {'jmeno':'Ondra', 'Prijmeni': 'Borec', 'Age': 23}

del dict['Prijmeni']

for key,val in dict.items():
    print(key, ' - ', val)