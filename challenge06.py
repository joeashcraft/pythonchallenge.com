#!/usr/bin/env python3
"""challenge06.

find the zip.
"""

import requests
import zipfile
import io

base_url = 'http://www.pythonchallenge.com/pc/def/channel.html'
zip_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'

resp = requests.get(zip_url)
resp_file = resp.content
my_file = io.BytesIO(resp_file)
my_zip = zipfile.ZipFile(my_file)

# file: readme.txt
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip


def read_file(fname):
        with my_zip.open(fname) as _file:
            return _file.read()

token = 90052
while True:
    fname = str(token)+'.txt'
    contents = read_file(fname).decode()
    comments = my_zip.getinfo(fname).comment.decode()
    try:
        token = contents.split()[3]
        # print(f"# file: {fname}")
        # print(contents)
        print(comments, end='')
        # print()
    except IndexError:
        print(contents)
        break
