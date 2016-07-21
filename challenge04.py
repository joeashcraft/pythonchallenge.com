"""challenge04.

follow the chain
"""

import urllib
import re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

first_page = urllib.urlopen(base_url + '?nothing=12345')
pagein = first_page.read()
# print type(pagein)
print pagein

next_page = re.search('and the next (\w) is (\w)', pagein)
next_page_param = next_page.group(1)
next_page_id = next_page.group(2)
