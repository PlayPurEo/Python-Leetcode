# author : 'wangzhong';
# date: 22/01/2021 14:13

"""
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，
如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max = 0
        l = r = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] - nums[i - 1] > 0:
                r = i
            else:
                if i - 1 == 0 or nums[i - 1] - nums[i - 2] > 0:
                    max = max(max, r - l + 1)
                l = r = i
        max = max(max, r - l + 1)
        return max