#_*_coding:utf-8 _*_

import numpy as np
import pandas as pd
import time

time_start=time.time()
data = []
frame = pd.DataFrame(range(0),index = range(1,3953),columns = ["Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"])
frame=frame.fillna(0)
for l in open("movies.dat"):
      rows = [str(x) for x in l.split("::")]
      a=int(rows[0])
      b=rows[2]
      b=str(b.strip('\n'))
      c = [str(x) for x in b.split("|")]

      #print 1213123
      for i in range(len(c)):
            classmovie=c[i]
            '''if classmovie=='Action':
                  col=0
            elif classmovie=='Adventure':
                  col=1
            elif classmovie=='Animation':
                  col=2
            elif classmovie=="Children's":
                  col=3
            elif classmovie=='Comedy':
                  col=4
            elif classmovie=='Crime':
                  col=5
            elif classmovie=='Documentary':
                  col=6
            elif classmovie=='Drama':
                  col=7
            elif classmovie=='Fantasy':
                  col=8
            elif classmovie == 'Film-Noir':
                  col =9
            elif classmovie == 'Horror':
                  col = 10
            elif classmovie == 'Musical':
                  col = 11
            elif classmovie == 'Mystery':
                  col = 12
            elif classmovie == 'Romance':
                  col = 13
            elif classmovie == 'Sci-Fi':
                  col = 14
            elif classmovie == 'Thriller':
                  col = 15
            elif classmovie == 'War':
                  col = 16
            else :
                  col=17'''
            #print type(col)
            frame.ix[a,classmovie]=1


frame.to_csv('MC.csv',index=False,header=False)
      #for i in len(c)




