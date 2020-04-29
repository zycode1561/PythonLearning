#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
s: str 给定的字符串
n: int 给定的行数
"""


def convert(s, n):
    if n < 2:
        return s
    res = ['' for _ in range(n)]
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == n - 1:
            flag = -flag
        i += flag
    return ''.join(res)


"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    str_x = str(x)
    x = ''
    if str_x[0] == '-':
        x += '-'
    x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
    x = int(x)
    if -2 ** 31 < x < 2 ** 31 - 1:
        return x
    return 0


print(reverse(-21474836))


def reverseURL(x: str) -> str:
    return '.'.join(reversed(x.split('.')))


print(reverseURL('www.baidu.com'))
