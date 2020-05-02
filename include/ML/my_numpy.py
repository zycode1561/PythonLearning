#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

import numpy

world = numpy.genfromtxt('/Users/zhangyun/Desktop/PythonWorkspace/test.txt', delimiter=',', dtype=str)

vector = numpy.array([12, 13, 14, 15])

matrix = numpy.array([[5, 10, 15], [20, 10, 30]])

equal_to_ten = (matrix == 10)

vector = vector.astype(float)

res1 = matrix.sum(axis=1)  # 每行进行相加

res2 = matrix.sum(axis=0)  # 每列进行相加

a = numpy.arange(15).reshape(3, 5)

a.ndim
a.shape
a.dtype.name
a.size
matrix0 = numpy.zeros((3, 4))
matrix1 = numpy.ones((3, 4))
numpy.arange(10, 30, 5)
numpy.arange(0, 2, 0.3)
matrix2 = numpy.random.random((2, 3))

# from numpy import pi
# print(numpy.linspace(0, 2*pi, 100)) # 0到2派，平均取100个数

a = matrix  # 这里是赋了引用，指向的内存区域是相同的
a = matrix.view()  # 浅复制，id不同，但是共用了值
a = matrix.copy()  # 复制之后互不影响
b = numpy.arange(6).reshape(2, 3)
c = a - b
a = a.T
A = numpy.array([[1, 1],
                 [0, 1]
                 ])
B = numpy.array([[2, 0],
                 [3, 4]
                 ])

C = numpy.dot(A, B)

A.dot(B)

numpy.exp(B[1, :])  # 计算e的多少次方
numpy.sqrt(B[1, :])  # 计算平方根

A.ravel()  # 把矩阵变成向量

A.T  # A的转置

D = A.reshape(1, -1)  # 确定第一个纬度之后第二个自动生成

E = numpy.hstack((A, B))  # 对A在右边直接拼接B

F = numpy.vstack((A, B))  # 对A在下面直接拼接B

numpy.hsplit(E, 2)  # 把A水平切分为三份
numpy.hsplit(E, (1, 2))  # 对E进行指定位置的切分

ind = c.argmax(axis=0)
data_max = c[ind, range(c.shape[1])]

x = numpy.arange(0, 40, 10)  # [0,40)区间，每隔10取一个数

y = numpy.tile(x, (5, 3))  # 对行和列进行扩展，行5倍，列3倍

z = numpy.array([
    [4, 3, 5],
    [1, 2, 1],
    [5, 9, 7]
])
z1 = numpy.sort(z, axis=1)  # 对每行进行排序,按列排序
z2 = numpy.sort(z, axis=0)  # 对每列进行排序，按行排序

a1 = numpy.matrix(A)
a2 = numpy.matrix(B)
