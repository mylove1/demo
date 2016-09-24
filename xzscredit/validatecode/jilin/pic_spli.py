# coding:utf-8
from PIL import Image
import time
import os
from image_deal_with import IMAGE

threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)


frompath = r'C:\\Users\\cooper\\Desktop\\opp\\jilin\\a'
topath = r'C:\\Users\\cooper\\Desktop\\opp\\jilin\\p'
for x, y, z in os.walk(frompath):
    for w in z:
        fname = os.path.join(x, w)
        print fname
        image = Image.open(fname)
        im = IMAGE(image)
        image = im.main()
        region = im.get_region_list()
        for enu,regi in enumerate(region):
            p = image.crop(regi)
            p.save(os.path.join(topath, w[:-3] + str(enu) + ".jpg"), 'BMP')

