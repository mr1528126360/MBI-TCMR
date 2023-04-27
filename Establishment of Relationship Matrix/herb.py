import pandas as pd
import re
import numpy as np
def herb( parameters ):
    # 读取必要的药方，化合物，基因和草药数据
    print("读取数据")
    drug = pd.read_csv("drug.csv", sep=",")
    Herb = pd.read_csv("草药.csv", sep=",")
    Herb_Com = pd.read_csv("草药-化合物.csv", sep=",")
    Com = pd.read_csv("化合物id.csv", sep=",")
    Com_Gen = pd.read_csv("化合物-基因关系.csv", sep=",")
    Gen = pd.read_csv("基因_id.csv", sep=",")
    pathway = pd.read_csv("pathway_fin.csv", sep=",")
    function = pd.read_csv("function.csv",sep=",")
    # 获取当前药方的草药，list3是当前药方的药物名称，for i in range(0,1):1是只使用一个药方
    print("获取当前药方的草药")
    b = 0
    list3 = []
    a = drug["fom"][drug.index[parameters]]
    b = 0
    for j in range(0, len(a)):
        if (a[j] == " "):
            # print(a[b:j])
            list3.append(a[b:j])
            b = j + 1
    # list1是草药的ID,list2是草药的C_ID
    print("获取草药ID")
    list1 = []
    list2 = []
    for i in range(0, len(list3)):
        for j in range(0, len(Herb["chinese"])):
            if (list3[i] == Herb["chinese"][j]):
                list1.append(Herb["ID"][j])
                list2.append(Herb["C_ID"][j])
    m1 = np.zeros((204))#草药权重
    m2 = np.zeros((13963, 204))#草药-化合物权重
    m3 = np.zeros((13963))#化合物权重
    m4 = np.zeros((11230, 13963))#化合物-基因权重
    m5 = np.zeros((11230))#基因权重
    m6 = np.zeros(([20861, 11230]))#基因-通路权重
    m7 = np.zeros((20861))#通路权重
    m8 = np.zeros((4608, 20861))#通路-功能权重
    m9 = np.zeros((4608))#功能权重
    # 计算m2和m3,list4是保留的草药坐标，list5是保留的化合物ID坐标,list6是保留的化合物的C_ID
    print("计算m2和m3")
    list4 = []
    list5 = []
    list6 = []
    for i in range(0, len(Herb_Com["草药ID"])):
        for j in range(0, len(list2)):
            if (Herb_Com["草药ID"][i] == list2[j]):
                list4.append(list1[j])
                list6.append(Herb_Com["化合物ID"][i])
                for k in range(0, len(Com["C_ID"])):
                    if (Com["C_ID"][k] == Herb_Com["化合物ID"][i]):
                        list5.append(Com["ID"][k])
    # 对保留的化合物坐标进行去重
    list6_1 = []
    for i in list6:
        if i not in list6_1:
            list6_1.append(i)
    list5_1 = []
    for i in list5:
        if i not in list5_1:
            list5_1.append(i)
    # list7是保留的化合物坐标，list8是保留的基因ID坐标,list9是保留的基因的C_ID
    print("计算m4和m5")
    list7 = []
    list8 = []
    list9 = []
    for i in range(0, len(Com_Gen["化合物ID"])):
        for j in range(0, len(list6_1)):
            if (Com_Gen["化合物ID"][i] == list6_1[j]):
                list7.append(list5_1[j])
                list9.append(Com_Gen["基因ID"][i])
                for k in range(0, len(Gen["C_ID"])):
                    if (Gen["C_ID"][k] == Com_Gen["基因ID"][i]):
                        list8.append(Gen["ID"][k])
    # 对保留的基因坐标进行去重
    list8_1 = []
    for i in list8:
        if i not in list8_1:
            list8_1.append(i)
    print("计算m6和m7")
    #list10为保留的通路的坐标，list11为保留的基因点的坐标
    list10 = []
    list11 = []
    for i in range(0,len(pathway["PARTICIPANT_A"])):
        for j in range(0,len(list8_1)):
            if (pathway["PARTICIPANT_A"][i] == Gen["Gene_name"][list8_1[j]] or pathway["PARTICIPANT_B"][i] == Gen["Gene_name"][list8_1[j]]):
                list10.append(i)
                list11.append(list8_1[j])
   #对于保留的通路坐标进行去重
    list10_1 = []
    for i in list10:
        if i not in list10_1:
            list10_1.append(i)
    print("计算m8和m9")
    #list12为保留的功能的坐标，list13为保留的通路的坐标
    list12 = []
    list13 = []
    for i in range(0,len(function["PATHWAY_NAMES"])):
        for j in range(len(list10_1)):
            if (function["PATHWAY_NAMES"][i] == pathway["PATHWAY_NAMES"][list10_1[j]]):
                list12.append(i)
                list13.append(list10_1[j])
    #对于保留的function进行去重
    list12_1 = []
    for i in list12:
        if i not in list12_1:
            list12_1.append(i)

    # 建立草药的0,1权重矩阵
    print("建立m1-m9权重矩阵")
    for i in range(0, len(list1)):
        m1[list1[i]] = 1
    ##建立草药-化合物，化合物的0,1权重矩阵
    for i in range(0, len(list5)):
        m2[list5[i]][list4[i]] = 1
    for i in range(0, len(list5_1)):
        m3[list5_1[i]] = 1
    for i in range(0,len(list7)):
        m4[list8[i]][list7[i]] = 1
    for i in range(0,len(list8_1)):
        m5[list8_1[i]] = 1
    for i in range(0,len(list10)):
        m6[list10[i]][list11[i]] = 1
    for i in range(0,len(list10_1)):
        m7[list10_1] = 1
    for i in range(0,len(list12)):
        m8[list12[i]][list13[i]] = 1
    for i in range(0,len(list12_1)):
        m9[list12_1] = 1
    print("done")
    return m1,m2,m3,m4,m5,m6,m7,m8,m9