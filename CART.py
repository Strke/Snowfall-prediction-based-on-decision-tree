import numpy as np
import pandas as pd
import pickle
from config import model_save_road
import random

class Cart:
    # 输入一个numpy类型的二维数据矩阵
    def __init__(self, x):
        self.data = x
        self.row = np.size(x, 0)  # 行数
        self.col = np.size(x, 1)  # 列数
        self.choose_col = 0
        self.choose_row = 0
        self.model_road = "BTree.pickle"
        self.model = []

    # p为一列的数据
    # p为输入的只有0和1的数据列
    def gini(self, p):
        yes = np.sum(p)
        no = self.row - yes
        res = 1 - (yes/self.row) ** 2 - (no/self.row) ** 2
        return res

    def buildTree(self, data_for_every_tree, k):
        # 停止条件
        n, m = np.shape(data_for_every_tree)
        judge = data_for_every_tree[:, m - 1].copy()
        g = np.sum(judge)
        if k + 1 == self.col:
            #if(g > n/2):
            #return ["YES"]
            #else:
            return ["YES"]
        if(g == 0):
            return ["NO"]
        if(g == n):
            return ["YES"]
        
        ans = []
        data_for_every_tree = data_for_every_tree[np.argsort(data_for_every_tree[:,k])] # 按所需比较的列总体排序
        import_col = data_for_every_tree[:,k].copy() # 拿出我们需要比较的一列
        import_col = import_col
        decision_col = [] # 计算所有分类值
        for i in range(n - 1):
            decision_col.append((import_col[i] + import_col[i + 1]) / 2)
        # 计算最优分类点
        gini_array = []
        # 首先枚举所有分类点
        for i in range(n -  1):
            bool_col = import_col > decision_col[i] # 得到01向量
            #print(bool_col)
            gini_array.append(self.gini(bool_col)) # 算出gini系数并放入数组
        pos = 0
        minn = 2
        for i in range(n - 1):
            if(gini_array[i] < minn):
                minn = gini_array[i]
                pos = i # 得到最优分类位置
        less_data = data_for_every_tree[0:pos,:].copy()
        greater_data = data_for_every_tree[pos + 1 : n - 1,:].copy()
        # print("root = ",minn,"left_size = ",np.shape(less_data),"right_size = ",np.shape(greater_data))
        ans.append(decision_col[pos])
        ans.append(self.buildTree(less_data,k+1))
        ans.append(self.buildTree(greater_data,k+1))
        return ans

    def train_model(self):
        res = []
        res = self.buildTree(self.data, 0)
        self.model = res
        
    def save_model(self, model):
        with open(self.model_road, 'wb') as f:
            pickle.dump(model, f)

    def load_model(self):
        with open(self.model_road, 'rb') as f:
            model = pickle.load(f)
        return model
    

def load_model():
    with open(model_save_road, 'rb') as f:
        model = pickle.load(f)
    return model