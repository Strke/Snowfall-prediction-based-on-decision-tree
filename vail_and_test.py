import pandas as pd
import numpy as np
from config import choose_feature, after_clean_saving_rate


def run(data, model, k):
    if (model[0] == 'NO') | (model[0] == 'YES'):
        return model[0]
    if data[k] <= model[0]:
        return run(data, model[1], k + 1)
    else:
        return run(data, model[2], k + 1)

def vail(data, model):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    n, m = np.shape(data)
    for j in range(m - 1):
        p = data[:, j]
        x = run(p, model, 0)
        if p[n - 1] == 0:
            if x == "NO":
                TN = TN + 1
            else:
                FP = FP + 1
        else:
            if x == "YES":
                TP = TP + 1
            else:
                FN = FN + 1
        #print(TP, TN, FP, FN)
    if TP + FP == 0:
        P = 0
    else:
        P = TP/(TP + FP)
    if TP + FN == 0:
        R = 0
    else:
        R = TP/(TP + FN)
    if (P == 0) | (R == 0) :
        F1 = 0
    else:
        F1 = (2 * P * R)/(P + R)
    print("ACC =  ", (TP + TN)/(TP + TN + FP + FN))
    print("Precision = ", P)
    print("Recall= ", R)
    print("F1-score= ", F1)
    
def vail_model(Btree, data):
    data = data.T
    vail(data, Btree)
    
def test_model(data, model):
    data = data.T
    n, m = np.shape(data)
    for j in range(m - 1):
        print(run(data[:, j], model, 0), "    ", data[n - 1][j])
    
    
    

