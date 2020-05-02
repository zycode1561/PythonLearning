#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:33:26 2020

@author: zhangyun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/zhangyun/Desktop/ML/wu_ML/andrew_ml_ex14179/ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

data.plot(kind='scatter', x='Population', y='Profit', figsize=(8, 6))
plt.show()


# J(theta)
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


data.insert(0, 'Ones', 1)  # 在data中加入一列ones，都为1

# 初始化x y
cols = data.shape[1]
X = data.iloc[:, :-1]  # 取前两列
y = data.iloc[:, cols - 1:cols]  # 取最后一列

# 转换为ndarray
X = np.matrix(X.values)
y = np.matrix(y.values)
# 初始化theta，不管选哪里都可以，都会下降到最低点
theta = np.matrix(np.array([0, 0]))

# 计算J(theta)
computeCost(X, y, theta)


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))  # 根据theta的纬度生成一个全0的矩阵
    parameters = int(theta.ravel().shape[1])  # ravel()扁平化，就是拉成一个行,theta列的个数，也就是长度
    cost = np.zeros(iters)  # cost就是计算出来的J(theta) iters是迭代次数

    for i in range(iters):
        error = (X * theta.T) - y  # 一个行向量*一个列向量，结果是行向量的每一个元素乘以列向量中的所有元素，生成对应的列
        # 注意：np.matrix之后的np.array的*相当于矩阵乘法
        for j in range(parameters):
            # 更新theta的公式学习率后面部分
            term = np.multiply(error, X[:, j])  # multiply(),矩阵的对应位置相乘
            # theta需要同时更新，所以先把结果存在一个temp的array中
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)
    return theta, cost


alpha = 0.01
iters = 1500

g, cost = gradientDescent(X, y, theta, alpha, iters)

predict1 = [1, 3.5] * g.T  
print("predict1:", predict1)
predict2 = [1, 7] * g.T
print("predict2:", predict2)

x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)  # 假设函数h(theta)，也就是线性回归的直线

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc='best')
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()
