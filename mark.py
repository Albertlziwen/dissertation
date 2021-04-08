# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:38:20 2021

@author: Albert
"""

import numpy as np
import pandas as pd
import coefficient as co
from coefficient import max2
from transition_matrix import dataframe,dataframe2,train,test,z

A = co.calA(dataframe,train)
B = co.calB(dataframe2,train)

AA = co.calA_j(dataframe,train)
BB = co.calB_ij(dataframe2,train)

te = z[0:len(test)+2][::-1]
mark=[]#系数与状态无关时的打分
mark2 = []#系数与状态有关时的打分

for i in range(len(test)):
  M = [0,0,0,0]
  
  for j in range(4):
    M[j]=A*dataframe[j][te[i+1]]/dataframe.loc[te[i+1],:].sum()+\
    B*dataframe2[j][4*te[i]+te[i+1]]/dataframe2.loc[4*te[i]+te[i+1],:].sum()
   
  if te[i+2]== M.index(max(M)):
    mark.append(1)
  elif te[i+2] == M.index(max2(M)):
    mark.append(0.5)
    
  else:
    mark.append(0)
    
for i in range(len(test)):
  M = [0,0,0,0]
  
  for j in range(4):
    M[j]=AA[te[i+1]]*dataframe[j][te[i+1]]/dataframe.loc[te[i+1],:].sum()+\
    BB[te[i]][te[i+1]]*dataframe2[j][4*te[i]+te[i+1]]/dataframe2.loc[4*te[i]+te[i+1],:].sum()
   
  if te[i+2]== M.index(max(M)):
    mark2.append(1)
  elif te[i+2] == M.index(max2(M)):
    mark2.append(0.5)
    
  else:
    mark2.append(0)