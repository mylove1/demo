# coding:utf-8
import os
from PIL import Image

flist = [str(x) for x in range(12)]

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


    # print the image in terminal
    # width, height = image.size
    # for y in range(height):
    #     for x in range(width):
    #         print image.getpixel((x, y)),
    #     print '\n'





    # 只计算一半
    # for y in range(height/2):
    #     count = 0
    #     for x in range(width/2):
    #         if image.getpixel((x, y)) == 0:
    #             count += 1
    #     tezhenglist.append(count)
    # for x in range(width/2):
    #     count = 0
    #     for y in range(height/2):
    #         if image.getpixel((x, y)) == 0:
    #             count += 1
    #     tezhenglist.append(count)


    # 最外一层黑点和
    #
    # x = 0
    # count = 0
    # for y in range(height):
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # for x in range(width):
    #     y = 0
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # y = 0
    # for x in range(width):
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # for y in range(height):
    #     x = 0
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    #     tezhenglist.append(count)
    # tezhenglist.append(count)
    #
    # # 最外二层黑点和
    # x = 1
    # count = 0
    # for y in range(height):
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # for x in range(width):
    #     y = 1
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # y = 1
    # for x in range(width):
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    # for y in range(height):
    #     x = 1
    #     if image.getpixel((x, y)) == 0:
    #         count += 1
    #     tezhenglist.append(count)
    # tezhenglist.append(count)

    return tezhenglist


threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

with open("ningxia.trainfile", 'w') as f:
    for this_file in flist:

        rootdir = os.path.join(r"C:\Users\cooper\Desktop\opp\ningxia\p", this_file)
        print rootdir
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                f.write(this_file)
                print this_file
                f.write(' ')
                filename = os.path.join(parent, filename)
                print filename
                image = Image.open(filename)
                # 把图像转为灰度图



                image = image.convert('L')
                image = image.point(table, '1')

                for enu, te in enumerate(tezheng(image)):
                    f.write("%d:%d" %(enu+1, te))
                    print enu+1,te
                    f.write("\t")
                f.write("\n")


