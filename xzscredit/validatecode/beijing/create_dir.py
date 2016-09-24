# coding:utf-8
import os


def mkdir(path, dir_list):
    for x in dir_list:
        os.mkdir(os.path.join(path, x))


def a_z():
    return [chr(x) for x in range(97, 97+26)]

def A_Z():
    return [chr(x) for x in range(65, 91)]

if __name__ == '__main__':
    dir_list = [str(x) for x in range(10)]
    path = r'C:\Users\cooper\Desktop\opp\beijing\p'
    # a_z
    dir_list.extend(a_z())
    # A_Z
    # dir_list.extend(A_Z())
    # print '\n'.join(dir_list)
    # print dir_list

    # 开始创建目录
    mkdir(path, dir_list)
