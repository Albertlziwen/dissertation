# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:46:45 2021

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


for i in range(4):
  t=i+2
  z=KMeans(n_clusters=t,random_state=9).fit_predict(X)
  plt.scatter(y,x,c=z)
  plt.show()
  s = silhouette_score(X, z)
  print("k="+str(t)+"时得分是"+str(s))