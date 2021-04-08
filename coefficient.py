# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:08:25 2021

@author: Albert
"""

import numpy as np
import pandas as pd

#求列表中第二大数
def max2(x):
    m1 = max(x)
    x2 = x.copy()
    x2.remove(m1)
    m2 = max(x2)
    return m2  
  
#系数A的计算,输入为训练集和一阶转移矩阵
def calA(dataframe,train):
  A = 0
  for i in range(len(train)-1):
    for j in range(4):
      if dataframe[j][train[i]]==dataframe.loc[train[i],:].max() and j==train[i+1]:
        A+=1
      elif dataframe[j][train[i]]==max2(dataframe.loc[train[i],:].to_list()) and j==train[i+1]:
        A+=0.5
  
  return A

def calB(dataframe2,train):
  B = 0
  for i in range(len(train)-2):
    for j in range(4):
      if dataframe2[j][train[i]*4+train[i+1]]==dataframe2.loc[train[i]*4+train[i+1],:].max() \
      and j==train[i+2]:
        B+=1
        
      elif dataframe2[j][train[i]*4+train[i+1]]==max2(dataframe2.loc[train[i]*4+train[i+1],:].to_list())\
      and j==train[i+2]:
        B+=0.5
      
  return B

#与状态有关的系数A_j,注意此时的输出是一个列表，包含了四个状态
def calA_j(dataframe,train):
  AA = [0,0,0,0]
  for i in range(4):
    for t in range(len(train)-1):
      middle = dataframe.loc[train[i],:].to_list()
      if train[t] == i and train[t+1]== middle.index(max(middle)):
        AA[i]+=1
      elif train[t]==i and train[t+1]==middle.index(max2(middle)):
        AA[i]+=0.5
        
  return AA

#与状态有关的系数B_ij,注意此时的输出是一个4*4的矩阵
def calB_ij(dataframe2,train):
  BB = np.array([0.1 for i in range(16)]).reshape(4,4)
  for i in range(4):
    for j in range(4):
      for t in range(len(train)-2):
        middle = dataframe2.loc[train[i]*4+train[j],:].to_list()
        if train[t]==i and train[t+1]==j:
          if train[t+2]==middle.index(max(middle)):
            BB[i][j]+=1
          elif train[t+2]==middle.index(max2(middle)):
            BB[i][j]+=0.5
            
  return BB






