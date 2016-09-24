# coding:utf-8
from PIL import Image


def black_white(image):
    value = 70
    width, hight = image.size
    for y in range(hight):
        for x in range(width):
            if image.getpixel((x, y))[0] >= value and image.getpixel((x, y))[1] >= value and image.getpixel((x, y))[2] >= value:
                image.putpixel((x, y), (255, 255, 255))
    return image


def del_noise(image, value):
    image1 = image
    threshold = 200
    image = to_l(image)
    image = to_two(image, threshold)
    width, height = image.size
    for y in range(height):
        for x in range(width):
            count = 0
            if x != 0 and x != (width-1) and y != 0 and y != (height-1):
                if image.getpixel((x, y)) == 0:
                    if image.getpixel((x - 1, y - 1)) == 1:
                        count += 1
                    if image.getpixel((x, y - 1)) == 1:
                        count += 1
                    if image.getpixel((x + 1, y - 1)) == 1:
                        count += 1
                    if image.getpixel((x - 1, y)) == 1:
                        count += 1
                    if image.getpixel((x + 1, y)) == 1:
                        count += 1
                    if image.getpixel((x - 1, y + 1)) == 1:
                        count += 1
                    if image.getpixel((x, y + 1)) == 1:
                        count += 1
                    if image.getpixel((x + 1, y + 1)) == 1:
                        count += 1

                if count >= value:
                    image1.putpixel((x, y), (255, 255, 255))
    return image1


def to_l(image):
    return image.convert('L')


def to_two(image, threshold):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table, '1')


def re_size(image, size):
    image.thumbnail(size)
    return image


def im_split(image, region):
    image.crop(region).show()





def clear(image):
    width, hight = image.size
    for y in range(hight):
        for x in range(width):
            pix = ()
            for enu, n in  enumerate(image.getpixel((x, y))):
                pix = pix + (n - n % 15,)
            # print pix
            image.putpixel((x, y), pix)
    return image


def im_tongji(image):
    tongji = {}
    width, hight = image.size
    for y in range(hight):
        for x in range(width):
            v = str(image.getpixel((x, y)))
            if v in tongji.keys():
                tongji[v] += 1
            else:
                tongji[v] = 1
    for x in tongji.keys():
        print x, tongji[x]

    return image


def xiangsi(a, b, v):
    if abs(a[0] - b[0]) <= 100 and abs(a[1] - b[1]) <= 30 and abs(a[2] - b[2]) <= v:
        return 1
    else:
        return 0



def jinsi(image):
    v = 10
    jinsizhi = {}
    width, hight = image.size
    for y in range(hight):
        for x in range(width):
            c = image.getpixel((x, y))
            for k in jinsizhi.keys():
                if xiangsi(jinsizhi[k], c, v):
                    jinsizhi[str(c)] = jinsizhi[k]
                    break
            if str(c) not in jinsizhi.keys():
                    jinsizhi[str(c)] = c
    for y in range(hight):
        for x in range(width):
            image.putpixel((x, y), jinsizhi[str(image.getpixel((x, y)))])
    return image


def im_view(image):
    print image.size
    print image.getpixel((140, 15))
    print image.getpixel((1, 1))
    print image.getpixel((195, 49))

def main(image):
    size = (60, 20)
    threshold = 200
    del_noise_value = 7
    image = black_white(image)
    image = del_noise(image, del_noise_value)
    image = del_noise(image, del_noise_value)
    # image = to_l(image)
    # image = to_two(image, threshold)
    # image = del_noise(image, del_noise_value)
    # image = re_size(image, size)
    return image

region_list = [(14, 5, 27, 19), (23, 5, 36, 19), (35, 5, 48, 19), (47, 5, 60, 19)]
if __name__ == '__main__':
    # image = Image.open(r".\011.jpg")
    # image = Image.open(r".\012.jpg")
    image = Image.open(r".\013.jpg")
    # image = Image.open(r".\014.jpg")
    # image = Image.open(r".\015.jpg")

    # im_view(image)


    # image = clear(image)
    image = main(image)

    image = jinsi(image)
    image = clear(image)

    im_tongji(image)





    # im_split(image, region_list[0])
    # im_split(image, region_list[1])
    # im_split(image, region_list[2])
    # im_split(image, region_list[3])

    image.show()