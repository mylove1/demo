# coding:utf-8
from svmutil import *
import os
import time

model_path = r".\ningxia.mo"
def train_svm_model():
    y, x = svm_read_problem(r".\ningxia.trainfile")
    model = svm_train(y, x)
    svm_save_model(model_path, model)
train_svm_model()


def svm_model_test():
    '''
    使用测试集进行测试
    :return:
    '''
    yt, xt = svm_read_problem("tezheng.txt")
    print yt
    print '-----------------'
    print xt
    model = svm_load_model("tianjin.mo")
    p_libel, p_acc, p_val = svm_predict(yt, xt, model)
    print p_libel, p_acc, p_val

# svm_model_test()

def svm_model_test_one():
    yt = [2,]
    xt = [{1: 1.0, 2: 0.0, 3: 1.0, 4: 0.0, 5: 1.0, 6: 1.0, 7: 3.0, 8: 1.0, 9: 1.0, 10: 3.0, 11: 2.0, 12: 0.0, 13: 0.0},]
    model = svm_load_model("C:/Users/cooper/Desktop/model")
    p_libel, p_acc, p_val = svm_predict(yt, xt, model)
    print type(p_libel)
    print p_libel[0]
    print p_libel, p_acc, p_val
# svm_model_test_one()
