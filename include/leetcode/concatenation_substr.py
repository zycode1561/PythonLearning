#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
滑动窗口，每次维护一个长度为words中所有单词长度的窗口
因为words中都是长度相等的单词，所以我们可以每隔一个长度截取一个单词
放入字典中，每个单词对应一个数量，判断这个字典和words形成的字典是否相同
用到了collections模块下的Counter
"""

__author__ = 'Zy_Code'

from collections import Counter


def findSubstring(s, words):
    if not s or not words:
        return []
    one_word = len(words[0])
    all_len = len(words) * one_word
    n = len(s)
    words = Counter(words)
    res = []
    for i in range(n - all_len + 1):
        temp = s[i:i + all_len]
        c_temp = []
        for j in range(0, all_len, one_word):
            c_temp.append(temp[j:j + one_word])
        if Counter(c_temp) == words:
            res.append(i)
    return res


print(findSubstring('barfoothefoobarman', ["foo", "bar"]))
