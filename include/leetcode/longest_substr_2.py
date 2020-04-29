#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""

__author__ = 'Zy_Code'


def lengthOfLongestSubstring(s: str) -> int:
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans


l = lengthOfLongestSubstring('helloWorld')
# print(l)

if 2 > 0 & 1 > 2/0:
    print(True)
