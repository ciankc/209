from collections import Counter
import sys
import time
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.models import load_model

class RoomMarkov():
    def __init__(self):
        df = pd.read_csv('datasets/dataset.csv')
        df = df.drop(['Activity', 'Time', 'timestamp'], axis = 1) 
        df = df[(df.T != 0).any()]
        df = df[(df == 1).sum(1) < 2]
        df_s = df

        # df.head(10)

        X_raw = df_s.values
        X = []
        rows = X_raw.shape[0]
        cols = X_raw.shape[1]
        for x in range(0, rows):
          for y in range(0, cols):
            if X_raw[x,y] == 1:
              X.append(y)
        # print(X)

        x0, x1, x2, x3, x4, x5 = [], [], [], [], [], []
        Xpair = [x0, x1, x2, x3, x4, x5]
        for i in range(len(X) - 1):
          if(X[i] == 0):
            Xpair[0].append(X[i+1])
          elif(X[i] == 1):
            Xpair[1].append(X[i+1])
          elif(X[i] == 2):
            Xpair[2].append(X[i+1])
          elif(X[i] == 3):
            Xpair[3].append(X[i+1])
          elif(X[i] == 4):
            Xpair[4].append(X[i+1])
          elif(X[i] == 5):
            Xpair[5].append(X[i+1])

        # print(Xpair)

        x0, x1, x2, x3, x4, x5 = [], [], [], [], [], []
        tX = [x0, x1, x2, x3, x4, x5]

        fin_t = []

        for j in range(6):
          c0, c1, c2, c3, c4, c5 = 0,0,0,0,0,0
          for i in range(len(Xpair[j])):
            if(Xpair[j][i] == 0):
              c0 = c0 + 1
            elif(Xpair[j][i] == 1):
              c1 = c1 + 1
            elif(Xpair[j][i] == 2):
              c2 = c2 + 1
            elif(Xpair[j][i] == 3):
              c3 = c3 + 1
            elif(Xpair[j][i] == 4):
              c4 = c4 + 1
            elif(Xpair[j][i] == 5):
              c5 = c5 + 1

          cnt = [c0, c1, c2, c3, c4, c5]
          tot = len(Xpair[j])
          
          for i in range(6):
            if(tot > 0):
              tX[j].append(round(cnt[i]/tot, 2))
          fin_t.append(tX[j])
          # print(fin_t)

        npa = np.asarray(fin_t, dtype=np.float32)
        two_step = npa.dot(npa)
        self.two_step = np.round(two_step, 4)
        # print(two_step)

    def get_top_two(self, srcRoom):
        row = self.two_step[srcRoom]
        m, mi = -1, -1
        sm, smi = -1, -1
        for i in range(len(row)):
            if row[i] > m:
                sm = m
                smi = mi
                m = row[i]
                mi = i
            elif row[i] > sm and sm < m:
                sm = row[i]
                smi = i
        
        # print(row)
        # print(m)
        # print(mi)
        # print(sm)
        # print(smi)
        return m, mi, sm, smi
