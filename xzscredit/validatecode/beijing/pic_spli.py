# coding:utf-8
from PIL import Image
import time
import os
from image_deal_with import main
from image_deal_with import region_list

frompath = r'C:\Users\cooper\Desktop\opp\beijing\a'
topath = r'C:\Users\cooper\Desktop\opp\beijing\p'
region = region_list


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