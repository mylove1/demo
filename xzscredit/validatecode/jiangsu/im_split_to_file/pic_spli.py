# coding:utf-8
from PIL import Image
import time
import os
from image_deal_with import main

frompath = r'C:\Users\cooper\Desktop\opp\jiangsu'
topath = r'C:\Users\cooper\Desktop\opp\jiangsu\p'
region = [(0, 8, 10, 19),
               (10, 8, 20, 19),
               (20, 8, 30, 19),
               (30, 8, 40, 19),
               (40, 8, 50, 19),
               (50, 8, 60, 19), ]


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