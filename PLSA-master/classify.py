# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import time

frame = pd.DataFrame(range(0), index=range(0, 10), columns=[range(0, 3952)])
frame = pd.read_csv('MU.csv', header=None, sep=',')


frame2 = pd.DataFrame(range(0), index=range(0, 3952), columns=["Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"])
frame2 = pd.read_csv('MC.csv', header=None, sep=',')
over=pd.DataFrame(range(0), index=range(0,10), columns=range(0,3))
X=frame.dot(frame2)
X.to_csv('UC.csv',index=False,header=False)

usern=X.shape[0]
classn=X.shape[1]
#print usern,classn
ucol=["Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
for u in range(0,usern):
    max =0
    for c in range(0,classn):
         if X.loc[u][c]>max:
            max=X.loc[u][c]
            ci=c

    print max,ci
    over.loc[u][0]=u+1
    over.loc[u][1]=ucol[ci]
    over.loc[u][2] = max

over.to_csv('usercalssp.csv',index=False,header=False)