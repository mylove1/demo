# coding:utf-8
from PIL import Image
import time
import os
from image_deal_with import main

frompath = r'C:\Users\cooper\Desktop\opp\chongqing\a'
topath = r'C:\Users\cooper\Desktop\opp\chongqing\p'
region = [(0, 10, 12, 40),
               (25, 10, 37, 40),
               (45, 10, 57, 40), ]


def split_all_pic(region, frompath, topath):
    for x, y, z in os.walk(frompath):
        for w in z:
            fname = os.path.join(x, w)
            print fname
            image = Image.open(fname)
            image = main(image)

            for enu,regi in enumerate(region):
                p = image.crop(regi)
                p.save(os.path.join(topath, w[:-3] + str(enu) + ".jpg"), 'BMP')

split_all_pic(region, frompath, topath)