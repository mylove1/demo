# coding:utf-8
from PIL import Image
from svmutil import *
import urllib2
import io

def convert_image(image):
    '''
    # 去噪，二值化处理
    :param image:
    :return:
    '''
    threshold = 100
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.convert('L')
    image = image.point(table, '1')
    image.thumbnail((100, 15))
    return image


def split(image):
    region = [(6, 3, 15, 11), (16, 3, 25, 11), (26, 3, 35, 11)]
    p1 = image.crop(region[0])
    p2 = image.crop(region[1])
    p3 = image.crop(region[2])
    return p1, p2, p3


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


def compute(d1, d2, d3):
    if d2 == 10:
        return add(d1, d3)
    elif d2 == 11:
        return cheng(d1, d3)
    else:
        return 'xx'


def add(d1, d2):
    return int(d1) + int(d2)

def cheng(d1, d2):
    return int(d1) * int(d2)

def tianjin_dist(image, model):
    # 去噪，二值化处理
    image = convert_image(image)
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


if __name__ == '__main__':
    model = svm_load_model("ningxia.mo")
    url = "http://gsxt.ngsh.gov.cn/ECPS/verificationCode.jsp?_=1474534287596"
    r = urllib2.urlopen(url)
    data_stream = io.BytesIO(r.read())
    image = Image.open(data_stream)
    image.show()
    # image = Image.open("C:/Users/cooper/Desktop/opp/ap/p/opp0.jpg")

    print tianjin_dist(image, model)

