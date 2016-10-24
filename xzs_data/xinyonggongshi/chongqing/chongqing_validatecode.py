# coding:utf-8
from PIL import Image
from svmutil import *
import urllib2
import io
from image_deal_with import main

def split(image):
    region = [(0, 10, 12, 40),
              (25, 10, 37, 40),
              (45, 10, 57, 40), ]

    p1 = image.crop(region[0])
    p2 = image.crop(region[1])
    p3 = image.crop(region[2])

    return p1, p2, p3

def compute(d1, d2, d3):
    if d2 == 10:
        return add(d1, d3)
    elif d2 == 11:
        return jian(d1, d3)
    else:
        return 'xx'


def add(d1, d2):
    return int(d1) + int(d2)

def jian(d1, d2):
    return int(d1) - int(d2)

def tezheng(image):
    tezhenglist = []
    width, height = image.size
    # for y in range(height):
    #     count = 0
    #     for x in range(width):
    #         if image.getpixel((x, y)) == 0:
    #             count += 1
    #     tezhenglist.append(count)
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


    p_libel, p_acc, p_val = svm_predict([0,], xt, model)

    # print "识别结果是：", p_libel[0]# , p_acc, p_val
    return p_libel[0]


def chongqing_dist(image, model):
    # 去噪，二值化处理
    image = main(image)
    # 图片分割为三部分
    p1, p2, p3 = split(image)
    # p1.show()
    # p2.show()
    # p3.show()
    d1 = distinguish(p1, model)
    d2 = distinguish(p2, model)
    d3 = distinguish(p3, model)
    result = compute(d1, d2, d3)
    return result


def chongqing_vali(text, model_file, show=False):
    if model_file:
        model = model_file
    else:
        model = svm_load_model("chongqing.mo")
    data_stream = io.BytesIO(text)
    image = Image.open(data_stream)
    if show:
        image.show()
    return chongqing_dist(image, model)

if __name__ == '__main__':
    model = svm_load_model("chongqing.mo")
    url = "http://gsxt.cqgs.gov.cn/sc.action?width=130&height=40&fs=23&t=1474620448546"

    r = urllib2.urlopen(url)
    data_stream = io.BytesIO(r.read())
    image = Image.open(data_stream)
    image.show()
    # image = Image.open("C:/Users/cooper/Desktop/opp/ap/p/opp0.jpg")

    print chongqing_dist(image, model)

