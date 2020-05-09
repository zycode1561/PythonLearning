#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:57:34 2020

@author: zhangyun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy.io import loadmat
from sklearn.metrics import classification_report  # 评价报告

data = loadmat('ex3data1.mat')

# 数据可视化

sample_idx = np.random.choice(np.arange(data['X'].shape[0]), 100)
sample_images = data['X'][sample_idx, :]

# nrows:创建subplot的行数，ncols：列数
fig, ax_array = plt.subplots(nrows=10, ncols=10, sharey=True, sharex=True, figsize=(12, 12))
for r in range(10):
    for c in range(10):
        ax_array[r, c].matshow(np.array(sample_images[10 * r + c].reshape((20, 20))).T, cmap=matplotlib.cm.binary)
        # plt.xticks([0,1],[1,2],rotation=0)
        # [0,1]代表x坐标轴的0和1位置，[2,3]代表0,1位置的显示lable，rotation代表lable显示的旋转角度。
        # 这里表示不显示坐标轴
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))

plt.show()


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    reg = (learningRate / (2 * len((X)))) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))
    return np.sum(first - second) / len(X) + reg


def gradient(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    error = sigmoid(X * theta.T) - y

    grad = ((X.T * error) / len(X)).T + ((learningRate / len(X)) * theta)

    grad[0, 0] = np.sum(np.multiply(error, X[:, 0])) / len(X)

    return np.array(grad).ravel()


from scipy.optimize import minimize


def one_vs_all(X, y, num_labels, leaning_rate):
    rows = X.shape[0]
    params = X.shape[1]
    all_theta = np.zeros((num_labels, params + 1))
    X = np.insert(X, 0, values=np.zeros(rows), axis=1)

    for i in range(1, num_labels + 1):
        theta = np.zeros(params + 1)
        y_i = np.array([1 if label == i else 0 for label in y])
        y_i = np.reshape(y_i, (rows, 1))

        fmin = minimize(fun=cost, x0=theta, args=(X, y_i, leaning_rate), method='TNC', jac=gradient)
        all_theta[i - 1, :] = fmin.x
    return all_theta


rows = data['X'].shape[0]
params = data['X'].shape[1]

all_theta = np.zeros((10, params + 1))
X = np.insert(data['X'], 0, values=np.zeros(rows), axis=1)

theta = np.zeros(params + 1)

y_0 = np.array([1 if label == 0 else 0 for label in data['y']])
y_0 = np.reshape(y_0, (rows, 1))

all_theta = one_vs_all(data['X'], data['y'], 10, 1)


def predict_all(X, all_theta):
    rows = X.shape[0]
    params = X.shape[1]
    num_labels = all_theta.shape[0]

    X = np.insert(X, 0, values=np.ones(rows), axis=1)

    X = np.matrix(X)

    all_theta = np.matrix(all_theta)

    h = sigmoid(X * all_theta.T)

    h_argmax = np.argmax(h, axis=1)
    h_argmax = h_argmax + 1
    return h_argmax


y_pred = predict_all(data['X'], all_theta)
print(classification_report(data['y'], y_pred))

# NeuralNetwork

weight = loadmat('ex3weights.mat')
theta1, theta2 = weight['Theta1'], weight['Theta2']

# 插入常数项
X2 = np.matrix(np.insert(data['X'], 0, values=np.ones(X.shape[0]), axis=1))
y2 = np.matrix(data['y'])

a1 = X2
z2 = a1 * theta1.T
a2 = sigmoid(z2)

a2 = np.insert(a2, 0, values=np.ones(a2.shape[0]), axis=1)
z3 = a2 * theta2.T
a3 = sigmoid(z3)

y_pred2 = np.argmax(a3, axis=1)+1
print(classification_report(y2, y_pred2))

