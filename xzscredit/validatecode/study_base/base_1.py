# coding:utf-8
from PIL import Image
import pytesseract

threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 打开图片
image = Image.open("1x5.jpg")

# 打印图片信息
print image.size
# 转换为灰度图
image = image.convert('L')

# 二值化
image = image.point(table, '1')

# 图片分割
region = (5, 2,25, 22)
p1 = image.crop(region)
# p1 = p1.rotate(45)
p1 = p1.resize((100, 100), Image.ANTIALIAS)
print p1.size
d1 = pytesseract.image_to_string(p1)

# 图片旋转
# p1 = p1.rotate(10)
# p1.show()

# region3 = (70, 2, 90, 22)
# p3 = image.crop(region3)
# d3 = pytesseract.image_to_string(p3)

# 保存图片
# p1.save("p1.jpg")
# p3.save("p3.jpg")
print d1
# print d3
# print 'start'
# 用默认图片查看器打开图片

# image.show()
p1.show()
# p3.show()