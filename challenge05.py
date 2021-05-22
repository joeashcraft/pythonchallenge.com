#!/usr/bin/env python3
"""challenge05.

pronounce it
"""

import requests
import pickle

base_url = 'http://www.pythonchallenge.com/pc/def/peak.html'
peakhell = 'http://www.pythonchallenge.com/pc/def/banner.p'

resp = requests.get(peakhell).content
my_obj = pickle.loads(resp)

# for k,v in [y for x in my_obj for y in x ]:
#   print(str(k) * int(v), end='')

for line in my_obj:
    for char,count in line:
        print(str(char) * int(count), end='')
    print()
