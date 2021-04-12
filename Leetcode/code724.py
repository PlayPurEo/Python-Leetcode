# author : 'wangzhong';
# date: 28/01/2021 15:08

"""
给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1