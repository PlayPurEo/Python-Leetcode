# author : 'wangzhong';
# date: 26/12/2020 01:18

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        temp = []
        check = [0 for _ in range(len(nums))]

        def helper(nums: List[int], start: int):
            if len(temp) == len(nums) or start == len(nums):
                return
            for i in range(start, len(nums)):
                if check[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                temp.append(nums[i])
                ans.append(list(temp))
                check[i] = 1
                helper(nums, i + 1)
                temp.pop()
                check[i] = 0
        helper(nums, 0)
        return ans