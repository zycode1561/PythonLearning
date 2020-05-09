#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用牛顿迭代法求零点问题
主要思想，找一点的切线与x轴相交的点作为新的横坐标，
不断逼近零点，直到x1，x0的差满足一定条件
"""

__author__ = 'Zy_Code'


def mySqrt(x: int):
    if x == 0:
        return 0
    C, x0 = float(x), float(x)
    while True:
        x1 = 0.5 * (x0 + C / x0)
        if abs(x0 - x1) < 1e-7:
            break
        x0 = x1
    return int(x0)


print(mySqrt(8))
