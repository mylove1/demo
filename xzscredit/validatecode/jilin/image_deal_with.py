# coding:utf-8
from PIL import Image


class IMAGE():
    def __init__(self, image):
        self.image = image

    def split(self, image, region):
        return image.crop(region)

    def niuqu(self, image, niu_list):
        '''
        把图像转正
        :param image:
        :param niu_list: 一个列表，分别为从图像最后一行的偏移量
        :return:
        '''
        width, hight = image.size
        for y in range(hight-1, -1, -1):
            for x in range(width-20):
                image.putpixel((x, y), image.getpixel((x + niu_list[y], y)))

        return image


    def black_white(self, image):
        value = 70
        width, hight = image.size
        for y in range(hight):
            for x in range(width):
                if image.getpixel((x, y))[0] >= value and image.getpixel((x, y))[1] >= value and image.getpixel((x, y))[2] >= value:
                    image.putpixel((x, y), (255, 255, 255))
        return image


    def del_noise(self, image, value):
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


    def to_l(self, image):
        return image.convert('L')


    def to_two(self, image, threshold):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return image.point(table, '1')


    def re_size(self, image, size):
        image.thumbnail(size)
        return image


    def im_split(self, image, region):
        image.crop(region).show()





    def clear(self, image):
        width, hight = image.size
        for y in range(hight):
            for x in range(width):
                pix = ()
                for enu, n in  enumerate(image.getpixel((x, y))):
                    pix = pix + (n - n % 15,)
                # print pix
                image.putpixel((x, y), pix)
        return image


    def im_tongji(self, image):
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


    def xiangsi(self, a, b, v):
        if abs(a[0] - b[0]) <= 100 and abs(a[1] - b[1]) <= 30 and abs(a[2] - b[2]) <= v:
            return 1
        else:
            return 0



    def jinsi(self, image):
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


    def im_view(self):
        image = self.main()
        print image.size
        # print image.getpixel((140, 15))
        # print image.getpixel((1, 1))
        # print image.getpixel((195, 49))

    def get_split_list(self, image):
        split_list = []
        del_list = []
        label = 0
        width, hight = image.size
        for x in range(width):
            count = 0
            for y in range(hight):
                if image.getpixel((x, y)) == label:
                    count += 1
            if count > 0:
                split_list.append(x)

        for x in range(len(split_list)):
            if split_list[x] -1 in split_list and split_list[x] + 1 in split_list:
                del_list.append(x)
        for x in del_list[::-1]:
            split_list.pop(x)
        return split_list

    def compose_region_list(self, l, region):
        region_list = []
        for x in range(len(l)/2):
            region_list.append((l[x*2], region[1], l[x*2+1], region[3]))
        return region_list


    def get_region_list(self):
        image = self.main()
        split_list = self.get_split_list(image)
        region_list = self.compose_region_list(split_list, (0, 0, 0, 19))
        return region_list




    def main(self):
        image = self.image
        size = (100, 10)
        threshold = 100
        del_noise_value = 7
        region = (0, 13, 250, 32)

        # 把图片上下的无用部分切除
        image = self.split(image, region)

        # 把图片的扭曲转正
        niu_list = [6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 3, 3, 3, 2, 2, 2, 1, 1, 0]
        image = self.niuqu(image, niu_list)
        image = self.to_l(image)
        image = self.to_two(image, threshold)

        image = self.re_size(image, size)


        # image = black_white(image)
        # image = del_noise(image, del_noise_value)
        # image = del_noise(image, del_noise_value)

        # image = del_noise(image, del_noise_value)
        # image = re_size(image, size)
        return image

# region_list = [(14, 5, 27, 19), (23, 5, 36, 19), (35, 5, 48, 19), (47, 5, 60, 19)]
if __name__ == '__main__':
    # image = Image.open(r".\0101.jpg")
    image = Image.open(r".\0102.jpg")
    # image = Image.open(r".\0103.jpg")
    # image = Image.open(r".\0104.jpg")
    # image = Image.open(r".\0105.jpg")
    im = IMAGE(image)
    image = im.main()
    im.im_view()

    # im_view(image)
    #
    #
    # image = main(image)


    # image = clear(image)




    # print region_list
    #
    # im_split(image, region_list[0])
    # im_split(image, region_list[1])
    # im_split(image, region_list[2])
    # im_split(image, region_list[3])




    # im_split(image, region_list[0])
    # im_split(image, region_list[1])
    # im_split(image, region_list[2])
    # im_split(image, region_list[3])

    image.show()