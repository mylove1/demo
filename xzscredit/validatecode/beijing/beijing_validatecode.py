# coding:utf-8
from PIL import Image
from svmutil import *
import urllib2
import io
from image_deal_with import main
from image_deal_with import region_list

def split(image):
    region = region_list

    p1 = image.crop(region[0])
    p2 = image.crop(region[1])
    p3 = image.crop(region[2])
    p4 = image.crop(region[3])

    return p1, p2, p3, p4


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
    p1, p2, p3, p4 = split(image)
    # p1.show()
    # p2.show()
    # p3.show()
    d1 = distinguish(p1, model)
    d2 = distinguish(p2, model)
    d3 = distinguish(p3, model)
    d4 = distinguish(p4, model)

    return [chr(int(d1)), chr(int(d2)), chr(int(d3)), chr(int(d4))]


if __name__ == '__main__':
    model = svm_load_model("beijing.mo")
    url = "http://qyxy.baic.gov.cn/CheckCodeCaptcha?currentTimeMillis=1474626756666&num=7585"

    r = urllib2.urlopen(url)
    data_stream = io.BytesIO(r.read())
    image = Image.open(data_stream)
    image.show()
    # image = Image.open("C:/Users/cooper/Desktop/opp/ap/p/opp0.jpg")

    print tianjin_dist(image, model)

