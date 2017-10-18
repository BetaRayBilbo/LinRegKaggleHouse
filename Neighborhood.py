# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:52:19 2017

@author: Ryan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read in training and test csv's
df=pd.read_csv('train.csv')
dftst=pd.read_csv('test.csv')

dfN=df[['Neighborhood','SalePrice']]

sns.set(style='whitegrid',color_codes=True)
sns.stripplot(x='Neighborhood', y='SalePrice', data=dfN, jitter=True)

dfN1=pd.get_dummies(dfN['Neighborhood'])
dfN1['SalePrice']=dfN['SalePrice']

A=dfN1.as_matrix()

b=A.shape[0]
c=A.shape[1]

for i in range(0,c):
    for j in range(0,b+1):
        