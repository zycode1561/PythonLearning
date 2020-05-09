#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

# coding=utf-8
from scipy.optimize import minimize
import numpy as np


# demo 1
# 计算 1/x+x 的最小值
def fun(args):
    a = args
    v = lambda x: a / x[0] + x[0]
    return v


if __name__ == "__main__":
    args = (1)  # a
    x0 = np.asarray((2))  # 初始猜测值
    res = minimize(fun(args), x0, method='SLSQP')
    print(res.fun)
    print(res.success)
    print(res.x)