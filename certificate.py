#!/usr/bin/env python

# import libraries
from PIL import Image, ImageDraw, ImageFont

# use a bitmap font
font = ImageFont.truetype("Helvetica.ttf", 25)

# open pre-exisiting template
img = Image.open('./certificate.jpg')

# draw image object
I1 = ImageDraw.Draw(img)

# add text to image
I1.text((800, 530), "Sharan Pai", font=font , fill=(0, 0, 0))

# save image
img.save("./certificate_output.jpg")
