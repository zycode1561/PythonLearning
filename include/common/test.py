#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给出一个整数 n，如果 n < 1，代表空树，否则代表中序遍历的结果为 {1, 2, 3... n}。
请输出可能的二叉树结构有多少。
解法：dp

注意1e9+7是一个float类型，如果不转int直接进行取模，产生的结果是浮点数，会造成错误
"""

__author__ = 'Zy_Code'

import math
from collections import Counter


lookup = Counter()

t = Counter('sdfsfgfh')

print(t)

print(list(map(lambda x: lookup[x] >= t[x], t.keys())))

all(map(lambda x: lookup[x] >= t[x], t.keys()))

print(-10 % 3)
print(1 % 3)
