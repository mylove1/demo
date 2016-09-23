# coding:utf-8
from PIL import Image
from svmutil import *
import urllib2
import io
from im_split_to_file.image_deal_with import main

def split(image):
    region = [(0, 8, 10, 19),
                   (10, 8, 20, 19),
                   (20, 8, 30, 19),
                   (30, 8, 40, 19),
                   (40, 8, 50, 19),
                   (50, 8, 60, 19), ]

    p1 = image.crop(region[0])
    p2 = image.crop(region[1])
    p3 = image.crop(region[2])
    p4 = image.crop(region[3])
    p5 = image.crop(region[4])
    p6 = image.crop(region[5])
    return p1, p2, p3, p4, p5, p6


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
    # print tezhenglist
    xt = [{},]
    for enu, x in enumerate(tezhenglist):
        xt[0][(enu+1)] = float(x)
    return xt


def distinguish(image, model):
    xt = tezheng(image)
    # print xt
    print '--'

    p_libel, p_acc, p_val = svm_predict([0,], xt, model)
    print '--'
    # print "识别结果是：", p_libel, p_acc, p_val
    return p_libel[0]


def tianjin_dist(image, model):
    # 去噪，二值化处理
    image = main(image)
    # 图片分割为三部分
    p1, p2, p3, p4, p5, p6 = split(image)
    # p1.show()
    # p2.show()
    # p3.show()
    d1 = distinguish(p1, model)
    d2 = distinguish(p2, model)
    d3 = distinguish(p3, model)
    d4 = distinguish(p4, model)
    d5 = distinguish(p5, model)
    d6 = distinguish(p6, model)
    return [chr(d1), chr(d2), chr(d3), chr(d4), chr(d5), chr(d6)]


if __name__ == '__main__':
    model = svm_load_model("jiangsu.mo")
    url = "http://www.jsgsj.gov.cn:58888/province/rand_img.jsp?type=7&temp=Fri%20Sep%2023%202016%2008:34:36%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)"

    r = urllib2.urlopen(url)
    data_stream = io.BytesIO(r.read())
    image = Image.open(data_stream)
    image.show()
    # image = Image.open("C:/Users/cooper/Desktop/opp/ap/p/opp0.jpg")

    print tianjin_dist(image, model)
