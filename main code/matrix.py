# -*- coding: utf-8 -*-
import pandas as pd
import re
import numpy as np
import torch
from sklearn.impute import SimpleImputer
import sys
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import os
 
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
 
        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        #return False
a = "F:\工作记录\中医药\数据集2\数据集"
a1 = "\m1.csv"
a2 = "\m2.csv"
a3 = "\m3.csv"
a4 = "\m4.csv"
a5 = "\m5.csv"
a6 = "\m6.csv"
a7 = "\m7.csv"
a8 = "\m8.csv"
a9 = "\m9.csv"
from herb import herb
for i in range(10,11):
    print(i)
    m1,m2,m3,m4,m5,m6,m7,m8,m9 = herb(i)
    b = str(i)
    c = a+b
    mkpath = c
    # 调用函数
    mkdir(mkpath)
    m1 = pd.DataFrame(m1)
    m2 = pd.DataFrame(m2)
    m3 = pd.DataFrame(m3)
    m4 = pd.DataFrame(m4)
    m5 = pd.DataFrame(m5)
    m6 = pd.DataFrame(m6)
    m7 = pd.DataFrame(m7)
    m8 = pd.DataFrame(m8)
    m9 = pd.DataFrame(m9)
    a1_1 = c+a1
    a2_2 = c+a2
    a3_3 = c+a3
    a4_4 = c+a4
    a5_5 = c+a5
    a6_6 = c+a6
    a7_7 = c+a7
    a8_8 = c+a8
    a9_9 = c+a9
    m1.to_csv(a1_1)
    m2.to_csv(a2_2)
    m3.to_csv(a3_3)
    m4.to_csv(a4_4)
    m5.to_csv(a5_5)
    m6.to_csv(a6_6)
    m7.to_csv(a7_7)
    m8.to_csv(a8_8)
    m9.to_csv(a9_9)