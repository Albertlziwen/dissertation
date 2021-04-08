# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:57:09 2021

@author: Albert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

name = "C:\\Users\\Albert\\Desktop\\WORK\\毕业设计\\Data.xlsx"
data = pd.read_excel(name,encoding = 'gbk')

x=data['纬度(°)']
xx=[t for t in x]
y=data['经度(°)']
yy=[t for t in y]

X=[]
for i in range(361):
  X.append([yy[i],xx[i]])
  
z=KMeans(n_clusters=4,random_state=9).fit_predict(X)

#逆序读数据
train = z[11:][::-1]
test = z[0:11][::-1]

#构建转移矩阵
dataframe = pd.DataFrame(np.array([0 for i in range(16)]).reshape(4,4))

for i in range(len(train)-1):
  dataframe[train[i+1]][train[i]]+=1
  
dataframe2 = pd.DataFrame(np.array([0 for i in range(64)]).reshape(16,4))

for i in range(len(train)-2):
  dataframe2[train[i+2]][train[i]*4+train[i+1]]+=1