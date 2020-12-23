# author : 'wangzhong';
# date: 10/12/2020 17:25

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        end = 0
        n = len(nums)
        ans = n + 1
        temp = 0
        while end < n:
            temp += nums[end]
            while temp >= s:
                ans = min(ans, end - start + 1)
                temp -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans