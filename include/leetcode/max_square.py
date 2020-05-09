#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


def maximalSquare(matrix) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    res = 0
    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                if j == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j])

    return res * res
