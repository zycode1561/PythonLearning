#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


def max_len1(k: int, nums: list):
    left, right, sum_0, n = 0, 0, 0, len(nums)
    # 先确定右边界
    while right < n:
        if nums[right] == 0:
            sum_0 += 1
        if sum_0 > k:
            break
        right += 1
    if right == n:
        return n
    right = right - 1
    ans = right - left + 1
    while right < n - 1:
        left = next_left(left, nums)
        right = next_right(right, nums)
        ans = max(ans, right - left + 1)
    return ans


def next_left(index, nums):
    while index < len(nums) and nums[index] == 1:
        index += 1
    return index + 1


def next_right(index, nums):
    while index + 1 < len(nums) and nums[index + 1] == 1:
        index += 1
    # 找到下一个0的下一位，还需要进行后面的1判断
    index += 1
    # 如果下一位是1
    if index + 1 < len(nums) and nums[index + 1] == 1:
        # 进行while循环一直找到最后一个1
        index += 1
        while index < len(nums) and nums[index] == 1:
            index += 1
        index -= 1
    return index


print(max_len1(0, [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]))

# 1 0 0 1 0 1 0 0 0 1 1 0 0 1 0 1 0 0 1
