import pandas as pd
import numpy as np
import random
from config import all_data_road, after_clean_saving_data, after_clean_saving_rate


# 主成分分析
def pca(dataset, k, x):
    n, m = np.shape(dataset)
    # cov为协方差矩阵
    cov = np.cov(dataset.astype(float))
    # a为特征值， b为特征向量
    a, b = np.linalg.eig(cov*(m-1)/m)
    c = np.array(list(range(1, 13)))
    a = np.vstack((a, c))
    a = a.T
    a = a[np.argsort(a[:, 0]), :]
    res = x[int(a[-1, 1])]
    for i in range(1, k):
        res = np.vstack([res, x[int(a[-1-i, 1])]])
    return a, res


def normalize(x):
    n, m = np.shape(x)
    max_arr = np.max(x, axis=1)
    min_arr = np.min(x, axis=1)
    for i in range(n):
        for j in range(m):
            if max_arr[i] == min_arr[i]:
                x[i, j] = 0
            else:
                x[i, j] = (x[i, j]-min_arr[i])/(max_arr[i]-min_arr[i])
    return x


def load_data():
    data = np.loadtxt(after_clean_saving_data, dtype=np.float, delimiter=',')
    return data


def data_load_clean(k):
    df = pd.read_csv(all_data_road)
    dataset = np.array(df)
    n, m = np.shape(dataset)
    dataset = dataset[0:n, 3:m]
    n, m = np.shape(dataset)
    for i in range(n):
        dataset[i, m-1] = int(dataset[i, m-1] == "YES")
    pos_example = dataset[1, :]
    neg_example = dataset[1, :]
    pos = 0
    neg = 0
    for i in range(n):
        if dataset[i, m - 1] == 1:
            # 由于正样本太少，把正样本额外存起来
            pos_example = np.vstack([pos_example, dataset[i, :]])
            pos = pos + 1
        else:
            neg_example = np.vstack([neg_example, dataset[i, :]])
            neg = neg + 1
    tnum = int(neg / pos / 4)
    dataset = dataset[1, :]
    for i in range(tnum):
        pos_example_1 = pos_example * 1.1
        pos_example_9 = pos_example * 0.9
        for t in pos_example_1:
            t[-1] = round(t[-1])
        dataset = np.vstack([dataset, pos_example_1])
        dataset = np.vstack([dataset, pos_example])
    dataset = np.vstack([dataset, neg_example])
    n, m = np.shape(dataset)
    # 防止nan的出现
    for i in range(0, n):
        for j in range(0, m):
            if np.isnan(dataset[i, j]):
                dataset[i, j] = (dataset[i - 1, j] + dataset[i - 2, j]) / 2
    dataset = dataset.T
    data = dataset.copy()
    n, m = np.shape(data)
    # 拆分标签和属性
    x = data[0:n - 1, :]
    y = data[n - 1, :]
    x = normalize(x)
    # 主成分分析，保留k个属性
    feature_sort, res = pca(x, k, dataset)
    res = np.vstack([res, y])
    res = res.T
    np.savetxt(after_clean_saving_data, res, delimiter=',', fmt='%s')
    np.savetxt(after_clean_saving_rate, feature_sort, delimiter=',', fmt='%s')
    n, m = np.shape(res)
    pos = n - neg
    return res, pos, neg


def split_tt(data, pos, neg):
    n, m = np.shape(data)
    ls_test = []
    ls_vail = []
    ls_train = []
    test_num = int(n / 32) * 4
    for i in range(int(test_num/2)):
        x = -1
        y = -1
        while (x < 0) | ((x in ls_test) & (y in ls_test)):
            x = random.randint(0, pos)
            y = random.randint(pos, n - 1)
        ls_test.append(x)
        ls_test.append(y)
    vail_num = int(n / 20) * 2
    for i in range(int(vail_num/2)):
        x = -1
        y = -1
        while (x < 0) | ((x in ls_test) & (y in ls_test)) | ((x in ls_vail) & (y in ls_vail)):
            x = random.randint(0, pos)
            y = random.randint(pos, n - 1)
        ls_vail.append(x)
        ls_vail.append(y)
    train_num = n - vail_num - test_num
    for i in range(n):
        if (i not in ls_test) & (i not in ls_vail):
            ls_train.append(i)
    train = data[ls_train[0]]
    test = data[ls_test[0]]
    vail = data[ls_vail[0]]
    for i in range(1, train_num):
        train = np.vstack([train, data[ls_train[i]]])
    for i in range(1, vail_num):
        vail = np.vstack([vail, data[ls_vail[i]]])
    for i in range(1, test_num):
        test = np.vstack([test, data[ls_test[i]]])
    n, m = np.shape(test)
    np.savetxt("test_data.csv", test[:, 0:m-1], delimiter=',')
    return train, vail, test

