# coding:utf-8
from PIL import Image
import pytesseract

var1 = {
    "12 12 9 11 11 11 11 11 8 12 12 12 12 12": 1,
    "12 12 8 11 11 11 11 12 8 12 12 12 12 12": 2,
    "12 12 8 11 10 9 11 10 8 12 12 12 12 12": 3,
    "12 12 11 10 10 10 6 11 11 12 12 12 12 12": 4,
    "12 12 8 11 9 10 11 11 9 12 12 12 12 12": 5,
    "12 12 9 11 10 9 10 10 9 12 12 12 12 12": 6,
    "12 12 8 11 12 11 11 11 11 12 12 12 12 12": 7,
    "12 12 9 10 9 9 10 10 8 12 12 12 12 12": 8,
    "12 12 9 10 10 10 9 11 8 12 12 12 12 12": 9,
}

var2 = {
    "13 12 12 11 9 10 11 12 9 10 13 13 13 13": "+",
    "13 12 12 11 9 11 11 12 9 10 13 13 13 13": "+",
    "13 10 12 8 8 12 7 12 10 12 13 13 13 13": "+",
    "13 11 12 8 8 12 7 12 10 12 13 13 13 13": "x",
}

var3 = {
    "12 12 9 11 11 11 11 11 8 12 12 12 12 12": 1,
    "12 12 8 11 11 11 11 12 8 12 12 12 12 12": 2,
    "12 12 8 11 10 9 11 10 8 12 12 12 12 12": 3,
    "12 12 11 10 10 10 7 11 11 12 12 12 12 12": 4,
    "12 12 8 11 9 10 11 11 9 12 12 12 12 12": 5,
    "12 12 9 11 10 9 10 10 9 12 12 12 12 12": 6,
    "12 12 8 11 12 11 11 11 11 12 12 12 12 12": 7,
    "12 12 9 10 9 9 10 10 8 12 12 12 12 12": 8,
    "12 12 9 10 10 10 9 11 8 12 12 12 12 12": 9,
}

threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 打开图片
# image = Image.open("1+4.jpg")
# image = Image.open("2+8.jpg")
# image = Image.open("2x2.jpg")
# image = Image.open("3+9.jpg")
# image = Image.open("4+2.jpg")
# image = Image.open("5x9.jpg")
# image = Image.open("6+1.jpg")
# image = Image.open("7+4.jpg")
# image = Image.open("9+2.jpg")
# image = Image.open("2x3.jpg")
image = Image.open("2.jpg")

# 打印图片信息
print image.size
# 转换为灰度图
image = image.convert('L')

# 二值化
image = image.point(table, '1')

# 图片缩放
image.thumbnail((100, 15))



for x in range(1, 7):
    for y in range(1, 7):
        print image.getpixel((y, x)),
    print '\n'

# total = 0
# tezhenglist = []
# for x in range(1, 15):
#     for y in range(3, 15):
#
#         total += image.getpixel((y, x))
#     tezhenglist.append(str(total))
#     total = 0
# v1 =  var1[' '.join(tezhenglist)]
#
# tezhenglist = []
# for x in range(1, 15):
#     for y in range(20, 33):
#
#         total += image.getpixel((y, x))
#     tezhenglist.append(str(total))
#     total = 0
# v2 = var2[' '.join(tezhenglist)]
#
# tezhenglist = []
# for x in range(1, 15):
#     for y in range(33, 45):
#
#         total += image.getpixel((y, x))
#     tezhenglist.append(str(total))
#     total = 0
# v3 = var3[' '.join(tezhenglist)]
# print v1, v2, v3

# 图片分割
# region = (5, 2,25, 22)
# p1 = image.crop(region)
# p1 = p1.rotate(45)
# p1 = p1.resize((100, 100), Image.ANTIALIAS)
# print p1.size
# d1 = pytesseract.image_to_string(p1)

# 图片旋转
# p1 = p1.rotate(10)
# p1.show()

# region3 = (70, 2, 90, 22)
# p3 = image.crop(region3)
# d3 = pytesseract.image_to_string(p3)

# 保存图片
# p1.save("p1.jpg")
# p3.save("p3.jpg")
# print d1
# print d3
# print 'start'
# 用默认图片查看器打开图片

image.show()
# p1.show()
# p3.show()