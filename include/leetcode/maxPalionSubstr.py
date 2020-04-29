#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""

__author__ = 'Zy_Code'


def longestPalindrome(s) -> str:
    n = len(s)
    p = [[False for i in range(n)] for j in range(n)]
    res = ''
    for length in range(1, n + 1):
        for start in range(n):
            end = start + length - 1
            if end >= n:
                break
            p[start][end] = (length == 1 or length == 2 or p[start + 1][end - 1]) and (s[start] == s[end])
            if p[start][end] and length > len(res):
                res = s[start:end + 1]
    return res


print(longestPalindrome('abaab'))

print(reversed())