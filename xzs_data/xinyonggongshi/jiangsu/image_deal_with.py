# coding:utf-8
from PIL import Image

def re_size(image, size):
    image.thumbnail(size)
    return image

def to_two(image, threshold):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table, '1')

def to_l(image):
    return image.convert('L')

def del_noise(image, value):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            count = 0
            if x != 0 and x != (width-1) and y != 0 and y != (height-1):
                if image.getpixel((x, y)) == 1:
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
                if image.getpixel((x, y)) == 0:
                    if image.getpixel((x - 1, y - 1)) == 0:
                        count += 1
                    if image.getpixel((x, y - 1)) == 0:
                        count += 1
                    if image.getpixel((x + 1, y - 1)) == 0:
                        count += 1
                    if image.getpixel((x - 1, y)) == 0:
                        count += 1
                    if image.getpixel((x + 1, y)) == 0:
                        count += 1
                    if image.getpixel((x - 1, y + 1)) == 0:
                        count += 1
                    if image.getpixel((x, y + 1)) == 0:
                        count += 1
                    if image.getpixel((x + 1, y + 1)) == 0:
                        count += 1
                if count <= value:
                    image.putpixel((x, y), (abs(image.getpixel((x, y)) -1)))
    return image

def im_split(region):
    image.crop(region).show()


def main(image):
    size = (120, 25)
    threshold = 177
    del_noise_value = 2
    image = to_l(image)
    image = to_two(image, threshold)
    image = del_noise(image, del_noise_value)
    image = re_size(image, size)
    return image

if __name__ == '__main__':
    imagepath = r'..\im.\35.jpg'
    imagepath = r'..\im.\949.jpg'
    # imagepath = r'..\im.\001.jpg'

    region_list = [(0, 8, 10, 19),
                   (10, 8, 20, 19),
                   (20, 8, 30, 19),
                   (30, 8, 40, 19),
                   (40, 8, 50, 19),
                   (50, 8, 60, 19),]

    # threshold 图片二值化的阈值点
    image = Image.open(imagepath)

    image = main(image)



    im_split(region_list[0])
    im_split(region_list[1])
    im_split(region_list[2])
    im_split(region_list[3])
    im_split(region_list[4])
    im_split(region_list[5])



    print image.size
    image.show()