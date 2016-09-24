# coding:utf-8
from PIL import Image



def im_view(image):
    print image.size
    print image.getpixel((140, 15))
    print image.getpixel((1, 1))

def black_white(image):
    width, hight = image.size
    for y in range(hight):
        for x in range(width):
            if image.getpixel((x, y))[0] + image.getpixel((x, y))[1] + image.getpixel((x, y))[2] <= 50:
                image.putpixel((x, y), (255, 255, 255))
    return image


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


def main(image):
    size = (60, 20)
    threshold = 200
    del_noise_value = 2
    image = black_white(image)
    image = to_l(image)
    image = to_two(image, threshold)
    image = del_noise(image, del_noise_value)
    image = re_size(image, size)
    return image



region_list = [(14, 5, 27, 19), (23, 5, 36, 19), (35, 5, 48, 19), (47, 5, 60, 19)]
if __name__ == '__main__':
    # image = Image.open(r".\11.jpg")
    # image = Image.open(r".\12.jpg")
    # image = Image.open(r".\13.jpg")
    image = Image.open(r".\14.jpg")
    im_view(image)

    image = main(image)



    im_split(image, region_list[0])
    im_split(image, region_list[1])
    im_split(image, region_list[2])
    im_split(image, region_list[3])

    image.show()