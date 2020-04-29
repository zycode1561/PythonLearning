#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


def threeSum(nums: list, target):
    n = len(nums)
    res = []
    if not nums or n < 3:
        return []
    nums.sort()
    ans = 2147483647
    for i in range(n):
        if nums[i] > target:
            return res
        l = i + 1
        r = n - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] - target < ans:
                res = [nums[i], nums[l], nums[r]]
                ans = nums[i] + nums[l] + nums[r] - target
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4], 1))
