#!/usr/bin/env python3
"""challenge04.

follow the chain
"""

import requests
import re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
param = "nothing"
token = 12345  # first token
token = 75635  # near the end
finished = False

while not finished:
    response = requests.get(base_url, params=dict([(param,token)])).content.decode()
    print(response)

    next_page = re.search('and the next ([a-zA-Z0-9_]*) is ([a-zA-Z0-9_]*)', response)
    if next_page:
        param = next_page.group(1)
        token = next_page.group(2)
    else:
        finished = True
