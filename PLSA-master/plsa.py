# -*- coding: utf-8 -*-
from numpy import zeros, int8, log
from pylab import random
import sys
import logging
import time
import codecs
import numpy as np
import pandas as pd
import math


# N : number of user
# M : number of movie
# X : document-word matrix, N*M, each line is the number of terms that show up in the document



def preprocessing():
    frame = pd.DataFrame(range(0), index=range(0, 10), columns=[range(0, 3952)])
    frame = pd.read_csv('datamean_10.csv', header=None, sep=',')
    N = frame.shape[0]
    M = frame.shape[1]
    X = frame
    # print X
    return N, M, X


def initializeParameters():
    for i in range(0, N):
        normalization = sum(lamda[i, :])
        for j in range(0, K):
            lamda[i, j] /= normalization;

    for i in range(0, K):
        normalization = sum(theta[i, :])
        for j in range(0, M):
            theta[i, j] /= normalization;


def EStep():
    for i in range(0, N):
        for j in range(0, M):
            denominator = 0;
            for k in range(0, K):
                p[i, j, k] = theta[k, j] * lamda[i, k];
                denominator += p[i, j, k];
          #  denominatorall[i, j] = denominator
            if denominator == 0:
                for k in range(0, K):
                    p[i, j, k] = 0;
            else:
                for k in range(0, K):
                    p[i, j, k] /= denominator;


def MStep():
    # update theta
    for k in range(0, K):
        denominator = 0
        for j in range(0, M):
            theta[k, j] = 0
            for i in range(0, N):
                theta[k, j] += X.loc[i, j] * p[i, j, k]
            denominator += theta[k, j]
        if denominator == 0:
            for j in range(0, M):
                theta[k, j] = 1.0 / M
        else:
            for j in range(0, M):
                theta[k, j] /= denominator
                # print theta[k,j]
    # update lamda
    for i in range(0, N):
        for k in range(0, K):
            lamda[i, k] = 0
            denominator = 0
            for j in range(0, M):
                # print lamda[i,k]
                # print X.loc[i,j]
                lamda[i, k] += X.loc[i, j] * p[i, j, k]
                denominator += X.loc[i, j];
            if denominator == 0:
                lamda[i, k] = 1.0 / K
            else:
                lamda[i, k] /= denominator
                # print lamda[i, k]


# calculate the log likelihood
def LogLikelihood():
    # print 'loglikelihood'
    loglikelihood = 0
    for i in range(0, N):
        for j in range(0, M):
            tmp = 0
            for k in range(0, K):
                tmp += theta[k, j] * lamda[i, k]
            if tmp > 0:
                loglikelihood += X.loc[i, j] * log(tmp)
    return loglikelihood


# output the params of model and top words of topics to files
def output():
    # user-rating distribution
    file = codecs.open(userRatingDist, 'w', 'utf-8')
    for i in range(0, N):
        tmp = ''
        for j in range(0, K):
            tmp += str(lamda[i, j]) + ' '
        file.write(tmp + '\n')
    file.close()

    # rating-Movie distribution
    file = codecs.open(ratingMovieDist, 'w', 'utf-8')
    for i in range(0, K):
        tmp = ''
        for j in range(0, M):
            tmp += str(theta[i, j]) + ' '
        file.write(tmp + '\n')
    file.close()

    # top movie of each rating
    file = codecs.open(ratingmovies, 'w', 'utf-8')
    for i in range(0, K):
        ratingmovie = []
        ids = theta[i, :].argsort()
        for j in ids:
            ratingmovie.insert(0, str(j))
            #  print theta[i,j]
        tmp = ''
        for movie in ratingmovie[0:min(ratingmoviesNum, len(ratingmovie))]:
            tmp += movie + ':' + str(theta[i, j]) + '  '
        file.write(tmp + '\n')
    file.close()


# set the default params and read the params from cmd
K = 18  # number of topic
maxIteration = 5
threshold = 1.0
ratingmoviesNum = 20
movieusersNum = 20
userRatingDist = 'userRatingDistribution.txt'
ratingMovieDist = 'ratingMovieDistDistribution.txt'
ratingmovies = 'ratingmovie.txt'
movieusers = 'movieusertxt'

# preprocessing
N, M, X = preprocessing()

# lamda[i, j] : p(zj|di)
lamda = random([N, K])
# print sum(lamda[1,:])
# theta[i, j] : p(wj|zi)
theta = random([K, M])

# p[i, j, k] : p(zk|di,wj)
p = zeros([N, M, K])
denominatorall = zeros([N, M])
# print p

initializeParameters()

# EM algorithm
oldLoglikelihood = 1
newLoglikelihood = 1
for d in range(0, maxIteration):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ' startEstep')
    EStep()

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ' startMstep')
    MStep()

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ' startlikelihood')
    newLoglikelihood = LogLikelihood()

    print("[", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "] ", d + 1, " iteration  ",
          str(newLoglikelihood))
    if (oldLoglikelihood != 1 and newLoglikelihood - oldLoglikelihood < threshold):
        break
    oldLoglikelihood = newLoglikelihood

frame2 = pd.DataFrame(range(0), index=range(0, 10), columns=[range(0, 3952)])
N2 = frame2.shape[0]
M2 = frame2.shape[1]
for i in range(0, N2):
    for j in range(0, M2):
        denominator1=0
        for k in range(0,k):
            p[i, j, k] = theta[k, j] * lamda[i, k];
            denominator1 += p[i, j, k];
            denominatorall[i, j] = denominator1
        frame2.loc[i][j] = denominatorall[i, j]

MU = frame2
MU.to_csv('MU.csv', index=False, header=False)
# output()
