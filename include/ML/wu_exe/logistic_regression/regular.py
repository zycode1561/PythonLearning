#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

path2 = 'ex2data2.txt'
data_init = pd.read_csv(path2, header=None, names=['Test1', 'Test2', 'Accepted'])

positive2 = data_init[data_init['Accepted'].isin([1])]
negative2 = data_init[data_init['Accepted'].isin([0])]

fig, ax3 = plt.subplots(figsize=(8, 6))
ax3.scatter(positive2['Test1'], positive2['Test2'], s=50, c='b', marker='o', label='Accepted')
ax3.scatter(negative2['Test1'], negative2['Test2'], s=50, c='r', marker='x', label='Rejected')
ax3.legend()
ax3.set_xlabel('Test 1 Score')
ax3.set_ylabel('Test 2 Score')
plt.show()

degree = 6
data2 = data_init
x1 = data2['Test1']
x2 = data2['Test2']
data2.insert(3, 'Ones', 1)

for i in range(1, degree + 1):
    for j in range(0, i + 1):
        data2['F' + str(i - j) + str(j)] = np.power(x1, i - j) * np.power(x2, j)

data2.drop('Test1', axis=1, inplace=True)
data2.drop('Test2', axis=1, inplace=True)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 实现正则化的代价函数
def costReg(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply(1 - y, np.log(1 - sigmoid(X * theta.T)))
    reg = (learningRate / (2 * len(X))) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))
    return np.sum(first - second) / len(X) + reg


# 实现正则化的梯度函数
def gradientReg(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid((X * theta.T)) - y

    for i in range(parameters):
        term = np.multiply(error, X[:, i])

        if i == 0:
            grad[i] = np.sum(term) / len(X)
        else:
            grad[i] = (np.sum(term) / len(X)) + ((learningRate / len(X)) * theta[:, i])

    return grad


def predict(theta, X):
    theta = np.matrix(theta)
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]


cols = data2.shape[1]
x2 = data2.iloc[:, 1:cols]
y2 = data2.iloc[:, 0:1]
theta2 = np.zeros(cols - 1)

x2 = np.array(x2)
y2 = np.array(y2)

learningRate = 1  # λ设为1

# 用库函数求解参数

result2 = opt.fmin_tnc(func=costReg, x0=theta2, fprime=gradientReg, args=(x2, y2, learningRate))

theta_min = np.matrix(result2[0])
predictions = predict(theta_min, x2)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y2)]
accuracy = (sum(map(int, correct)) % len(correct))
print('accuracy = {0}%'.format(accuracy))


# 画决策曲线

def hfunc2(theta, x1, x2):
    temp = theta[0][0]
    place = 0
    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            temp += np.power(x1, i - j) * np.power(x2, j) * theta[0][place + 1]
            place += 1
    return temp


def find_decision_boundary(theta):
    t1 = np.linspace(-1, 1.5, 1000)
    t2 = np.linspace(-1, 1.5, 1000)

    cordinates = [(x, y) for x in t1 for y in t2]
    x_cord, y_cord = zip(*cordinates)
    h_val = pd.DataFrame({'x1': x_cord, 'x2': y_cord})
    h_val['hval'] = hfunc2(theta, h_val['x1'], h_val['x2'])

    decision = h_val[np.abs(h_val['hval']) < 2 * 10 ** -3]

    return decision.x1, decision.x2


fig, ax4 = plt.subplots(figsize=(8, 6))

ax4.scatter(positive2['Test1'], positive2['Test2'], s=50, c='b', marker='o', label='Accepted')
ax4.scatter(negative2['Test1'], negative2['Test2'], s=50, c='r', marker='x', label='Rejected')
ax4.set_xlabel('Test 1 Score')
ax4.set_ylabel('Test 2 Score')

x, y = find_decision_boundary(result2)
plt.scatter(x, y, c='y', s=10, label='Prediction')
ax4.legend()
plt.show()
