# author : 'wangzhong';
# date: 26/12/2020 01:47

"""
子集2
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        temp = []
        check = [0 for _ in range(len(nums))]

        def helper(nums: List[int], start: int):
            if len(temp) == len(nums):
                return
            for i in range(start, len(nums)):
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