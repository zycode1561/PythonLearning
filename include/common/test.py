#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

num = 198
num //= 10
print(num)

s = [1, 2, 3, 4]
print(s[-1])


def divide(dividend, divisor):
    # 这里我们先取绝对值，后面根据异或运算来判断结果是正还是负
    i, a, b = 0, abs(dividend), abs(divisor)
    # 如果被除数为0或者被除数小于除数就退出递归
    if a == 0 or a < b:
        return 0
    # 当输出小于被除数的时候，对除数进行左移加倍，并记录倍数
    while b <= a:
        b = b << 1
        i = i + 1
    # 本次递归减去除数的个数，加上下次递归要减去除数的个数，注意要恢复被除数
    res = (1 << (i - 1)) + divide(a - (b >> 1), abs(divisor))
    if (dividend ^ divisor) < 0:
        res = -res
    # 因为题设可知最小值不可能越界，我们判断最大值是否越界即可
    return min(res, (1 << 31) - 1)


print(divide(2147483647, 1))
