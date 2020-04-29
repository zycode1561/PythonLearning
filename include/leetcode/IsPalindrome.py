#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


def isPalindrome(x: int):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    n = 0
    while x > n:
        n = n * 10 + x % 10
        x //= 10
    return x == n or x == n // 10


print(isPalindrome(-121))


class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


s = Solution()

print('isMatch? result = ', s.isMatch('aa', 'aa**'))


def maxArea(height) -> int:
    i, j, ans = 0, len(height) - 1, 0
    while i < j:
        ans = max(min(height[i], height[j]) * (j - i), ans)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return ans


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(heights))
