# coding:utf-8
"""
刚刚试了试转换分割后的图片，直接不识别，把以前法院的验证码拿来分割试试
"""
from PIL import Image
import pytesseract

threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = Image.open("1x5.jpg")
print image.size
image = image.convert("L")
image = image.point(table, '1')


region = (2, 2, 25, 22)
image = image.crop(region)
for x in range(0, 24):
    for y in range(0, 21):
        print image.getpixel((y, x)),
    print '\n'
for x in range(0, 24):
    for y in range(0, 21):
        print image.getpixel((y, x)),' ',
print image.getpixel((0, 0))



# print pytesseract.image_to_string(image)
image.show()