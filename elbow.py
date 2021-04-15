# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:40:37 2021

@author: Albert
"""
#手肘法
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
  
SSE = []
for k in range(1,9):
  estimator = KMeans(n_clusters=k)
  estimator.fit(X)
  SSE.append(estimator.inertia_)

T = range(1,9)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(T,SSE)
plt.show()