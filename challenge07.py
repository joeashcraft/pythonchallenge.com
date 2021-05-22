#!/usr/bin/env python3
"""challenge07.

smarty
"""

# import requests
import os
import io
from PIL import Image

base_url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
image_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
image_local = '~/Downloads/oxygen.png'

# resp = requests.get(image_url)
# image_file = Image.open(resp.content)
with open(os.path.expanduser(image_local),'rb') as file:
  my_image=Image.open(file)
  gray_bar = my_image.crop(box=(0,43,608,43+9))
px = gray_bar.load()

level_1 = "".join([chr(px[x,1][0]) for x in range(0,gray_bar.width,7)])
level_2 = level_1[level_1.find('['):]  #  '[105, 110, 116, 101, 103, 114, 105, 116, 121]'
level_2 = [ii for ii in map(int,level_2[1:-1].split(','))]  # [105, 110, 116, 101, 103, 114, 105, 116, 121]
level_2 = "".join([c for c in map(chr, level_2)])  # integrity

print(level_2)
