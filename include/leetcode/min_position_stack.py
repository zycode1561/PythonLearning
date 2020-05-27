#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个可能含有重复值的数组 arr，找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置。
返回所有位置相应的信息。

input:
    7
    3 4 1 5 6 2 7
output:
    -1 2
    0 2
    -1 -1
    2 5
    3 5
    2 -1
    5 -1

解法：单调栈
"""

__author__ = 'Zy_Code'


def solution(s, arr):
    stack, res = [-1], [[-1, -1] for _ in range(s)]
    for i in range(s):
        if stack[-1] == -1:
            stack.append(i)
            continue
        while arr[i] <= arr[stack[-1]] and stack[-1] != -1:
            stack.pop()
        res[i][0] = stack[-1]
        stack.append(i)
    stack = [-1]
    for i in range(s - 1, -1, -1):
        if stack[-1] == -1:
            stack.append(i)
            continue
        while arr[i] <= arr[stack[-1]] and stack[-1] != -1:
            stack.pop()
        res[i][1] = stack[-1]
        stack.append(i)
    return res


while True:
    try:
        s = int(input())
        arr = list(map(int, input().split()))
        res = solution(s, arr)
        for i in res:
            print(i[0], i[1])
    except:
        break
