# -*- coding: utf-8 -*-
from pylab import random
import sys
import time
import codecs
import numpy as np
import pandas as pd
import math
# N : number of user
# M : number of movie
# X : document-word matrix, N*M, each line is the number of terms that show up in the document


def preprocessing():

    frame = pd.DataFrame(range(0),index = range(0,10),columns = [range(0,3953)])
    frame=pd.read_csv('umratingNan_10.csv', header=None, sep=',')
    N=frame.shape[0]
    M=frame.shape[1]
    X=frame.fillna(0)
    Mean=[]
    Mean=X.mean()
   # print type(N)
    for i in range(0,N):
        for j in range(0,M):
            if X.loc[i][j]==0:
                X.loc[i][j]=Mean[j]

   # X=frame.fillna(0)
    X.to_csv('datamean_10.csv',index=False,header=False)

    return N, M, X
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  , ' startpreprocessing' )
preprocessing()
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  , ' end' )