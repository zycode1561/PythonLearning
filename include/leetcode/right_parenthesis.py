#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

__author__ = 'Zy_Code'

"""
回溯法，添加括号的时候，如果右括号的数量小于做括号的数量
就添加一个右括号，这样就可以保证整体的有效性，不用再去做合法性的判断
"""


def generateParenthesis(n: int) -> list:
    ans = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            ans.append(''.join(s))
            return
        if left < n:
            s.append('(')
            backtrack(s, left + 1, right)
            s.pop()
        if right < left:
            s.append(')')
            backtrack(s, left, right + 1)
            s.pop()

    backtrack([], 0, 0)
    return ans


print(generateParenthesis(3))

"""
动态规划
主要思想在于，每次其实就是加一对括号，这对括号加在哪里，怎么加是根本问题
每次加括号要保证加完之后是合法的，这时候我们就可以使用到前面计算出来的结果
让我们加的这对括号中包含一组括号，括号外面也包含一组括号，两个组的括号总对数为n - 1
这就是一种递归，并且每次都会用到前面的计算结果，所以可以用一个dp存储结果
"""


def generateParenthesis_dp(n: int) -> list:
    if n == 0:
        return []
    dp = [None for _ in range(n + 1)]
    dp[0] = ['']
    for i in range(1, n + 1):
        cur = []
        for j in range(i):
            left = dp[j]
            right = dp[i - j - 1]
            for s1 in left:
                for s2 in right:
                    cur.append('(' + s1 + ')' + s2)
        dp[i] = cur
    return dp[n]


print(generateParenthesis_dp(3))
