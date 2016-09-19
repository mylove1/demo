# coding:utf-8
import os
from PIL import Image

flist = [str(x) for x in range(1, 10)]
flist.extend(["0", "11"])
print flist

def tezheng(image):
    tezhenglist = []
    width, height = image.size
    for y in range(height):
        count = 0
        for x in range(width):
            if image.getpixel((x, y)) == 0:
                count += 1
        tezhenglist.append(count)
    for x in range(width):
        count = 0
        for y in range(height):
            if image.getpixel((x, y)) == 0:
                count += 1
        tezhenglist.append(count)

    # 最外一层黑点和

    x = 0
    count = 0
    for y in range(height):
        if image.getpixel((x, y)) == 0:
            count += 1
    for x in range(width):
        y = 0
        if image.getpixel((x, y)) == 0:
            count += 1
    y = 0
    for x in range(width):
        if image.getpixel((x, y)) == 0:
            count += 1
    for y in range(height):
        x = 0
        if image.getpixel((x, y)) == 0:
            count += 1
        tezhenglist.append(count)
    tezhenglist.append(count)

    # 最外二层黑点和
    x = 1
    count = 0
    for y in range(height):
        if image.getpixel((x, y)) == 0:
            count += 1
    for x in range(width):
        y = 1
        if image.getpixel((x, y)) == 0:
            count += 1
    y = 1
    for x in range(width):
        if image.getpixel((x, y)) == 0:
            count += 1
    for y in range(height):
        x = 1
        if image.getpixel((x, y)) == 0:
            count += 1
        tezhenglist.append(count)
    tezhenglist.append(count)

    return tezhenglist

with open("tezheng.txt", 'w') as f:
    for this_file in flist:

        rootdir = os.path.join("C:\Users\cooper\Desktop\opp\sp", this_file)
        print rootdir
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                f.write(this_file)
                f.write('\t')
                filename = os.path.join(parent, filename)
                print filename
                image = Image.open(filename)
                for enu, te in enumerate(tezheng(image)):
                    f.write("%d:%d" %(enu+1, te))
                    f.write("\t")
                f.write("\n")


