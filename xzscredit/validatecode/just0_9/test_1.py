# coding:utf-8
'''
使用pytesseract库来识别验证码
'''
from PIL import Image
import pytesseract

image = Image.open('0366.jpg')
vcode = pytesseract.image_to_string(image)
# act.image_to_string(image)
print vcode
