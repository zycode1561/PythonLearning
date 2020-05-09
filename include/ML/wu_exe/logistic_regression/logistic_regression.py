#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

path1 = 'ex2data1.txt'
data1 = pd.read_csv(path1, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])

positive = data1[data1['Admitted'].isin([1])]
negative = data1[data1['Admitted'].isin([0])]

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
# s表示点的面积， c为点的颜色， maker表示点的形状， alpha表示点的透明度
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
ax.legend(loc='best')
ax.set_xlabel('Exam 1 score')
ax.set_ylabel('Exam 2 score')
plt.show()


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply(1 - y, np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / len(X)


data1.insert(0, 'Ones', 1)
cols = data1.shape[1]
X = data1.iloc[:, 0:cols - 1]
y = data1.iloc[:, cols - 1: cols]
theta = np.zeros(3)

X = np.array(X.values)
y = np.array(y.values)


def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid((X * theta.T)) - y

    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        grad[i] = np.sum(term) / len(X)

    return grad


# 这里我们调用一个已有的库，我们不用自己定义迭代次数和步长，共呢个会直接告诉我们最优解

result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))

plotting_x1 = np.linspace(30, 100, 100)
# 根据h（theta）化简的x2和x1的对应关系
plotting_h1 = (- result[0][0] - result[0][1] * plotting_x1) / result[0][2]

fig, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(plotting_x1, plotting_h1, 'y', label='Prediction')
ax2.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
# s表示点的面积， c为点的颜色， maker表示点的形状， alpha表示点的透明度
ax2.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
ax2.legend(loc='best')
ax2.set_xlabel('Exam 1 score')
ax2.set_ylabel('Exam 2 score')
plt.show()


# 实现h(theta)
def hfunc1(theta, X):
    return sigmoid(np.dot(theta.T, X))


def predict(theta, X):
    theta = np.matrix(theta)
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]


theta_min = np.matrix(result[0])
predictions = predict(theta_min, X)
# zip函数可以让两个元素，依次组合成一个元组组成的列表
# a = [1,2,3]
# b = [4,5,6]
# zip(a, b) -> [(1, 4), (2, 5), (3, 6)]
# 以最短的为基准，长的后面会被舍弃
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
# 这里的map(int,correct)表示将correct转换成一个全为int的列表
accuracy = (sum(map(int, correct)) % len(correct))
print('accuracy = {0}%'.format(accuracy))



