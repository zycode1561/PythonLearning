#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


def pick_rain(height):
    ans, curr, n = 0, 0, len(height)
    stack = []
    while curr < n:
        while stack and height[curr] > height[stack[-1]]:
            h = height[stack.pop()]
            if not stack:
                break
            distance = curr - stack[-1] - 1
            min_h = min(height[stack[-1]], height[curr])
            ans += distance * (min_h - h)
        stack.append(curr)
        curr += 1
    return ans


print(pick_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
