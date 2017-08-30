import os,sys
import numpy as np
import pandas as pd

df=pd.read_csv("test.csv")
l1=df['0'].tolist()
l2=df['1'].tolist()
l=[]
[l.append(i) for i in l1 if i in l2]
print(l)            
