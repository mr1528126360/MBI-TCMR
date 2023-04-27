import pandas as pd
import numpy as np
a = "F:\工作记录\中医药\数据集2"
a1 = "m1.csv"
a2 = "m2.csv"
a3 = "m3.csv"
a4 = "m4.csv"
a5 = "m5.csv"
a6 = "m6.csv"
a7 = "m7.csv"
a8 = "m8.csv"
a9 = "m9.csv"
def read_file(i):
    #print(i)
    b = str(i)
    c = a+"\\"+b
    #print(c)
    #mkpath = c
    # 调用函数
    a1_1 = c+"\\"+a1
    a2_2 = c+"\\"+a2
    a3_3 = c+"\\"+a3
    a4_4 = c+"\\"+a4
    a5_5 = c+"\\"+a5
    a6_6 = c+"\\"+a6
    a7_7 = c+"\\"+a7
    a8_8 = c+"\\"+a8
    a9_9 = c+"\\"+a9
    m1 = pd.read_csv(a1_1, index_col=0)
    m2 = pd.read_csv(a2_2, index_col=0)
    m3 = pd.read_csv(a3_3, index_col=0)
    m4 = pd.read_csv(a4_4, index_col=0)
    m5 = pd.read_csv(a5_5, index_col=0)
    m6 = pd.read_csv(a6_6, index_col=0)
    m7 = pd.read_csv(a7_7, index_col=0)
    m8 = pd.read_csv(a8_8, index_col=0)
    m9 = pd.read_csv(a9_9, index_col=0)
    m1 = np.array(m1)
    m2 = np.array(m2)
    m3 = np.array(m3)
    m4 = np.array(m4)
    m5 = np.array(m5)
    m6 = np.array(m6)
    m7 = np.array(m7)
    m8 = np.array(m8)
    m9 = np.array(m9)
    return m1,m2,m3,m4,m5,m6,m7,m8,m9