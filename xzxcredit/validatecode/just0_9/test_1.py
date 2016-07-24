# coding:utf-8
'''
使用pytesseract库来识别验证码
'''
import pytesseract
from PIL import Image
import pytesser

image = Image.open('0366.jpg')
vcode = pytesser.image_to_string(image)
# act.image_to_string(image)
print vcode