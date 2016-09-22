# coding:utf-8
from PIL import Image
import time
import os

threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

path = 'C:\\Users\\cooper\\Desktop\\opp\\ningxia'
for x, y, z in os.walk(path):
    for w in z:
        fname = os.path.join(x, w)
        print fname
        image = Image.open(fname)
        # 转换为灰度图
        image = image.convert('L')
        # 二值化
        image = image.point(table, '1')
        # 图片缩放
        image.thumbnail((100, 15))

        region = [(6, 3, 15, 11), (16, 3, 25, 11), (26, 3, 35, 11)]
        for enu,regi in enumerate(region):
            p = image.crop(regi)
            p.save(os.path.join("C:\\Users\\cooper\\Desktop\\opp\\ningxia\\p", str(time.time()) + str(enu) + ".jpg"), 'BMP')

