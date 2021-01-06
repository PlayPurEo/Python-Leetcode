# author : 'wangzhong';
# date: 29/12/2020 22:53

"""
给定一个已排序的正整数数组 nums，和一个正整数 n 。
从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
请输出满足上述要求的最少需要补充的数字个数。
"""
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        index = 0
        length = len(nums)
        total = 0
        while total < n:
            if index < length and nums[index] <= total + 1:
                total += nums[index]
                index += 1
            else:
                total = total + total + 1
                count += 1
        return count