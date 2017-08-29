import os,sys
import numpy as np
import pandas as pd

df=pd.read_csv("test.csv")
l1=df['0'].tolist()
l2=df['1'].tolist()
l=[]
for i in l1:
    for j in l2:
        if i == j:
            l.append(i)

print(l)            
