# author : 'wangzhong';
# date: 07/02/2021 14:09

"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
        return True