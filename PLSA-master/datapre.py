#_*_coding:utf-8 _*_
import numpy as np
import pandas as pd
import time

time_start=time.time()
data = []
frame = pd.DataFrame(range(0),index = range(1,6041),columns = range(1,3953))

for l in open("ratings.dat"):
      rows = [int(x) for x in l.split("::")]
      a=rows[0]
      b=rows[1]
      c=rows[2]
      frame.loc[a][b]=c

frame.to_csv('umratingNan.csv',index=False,header=False)