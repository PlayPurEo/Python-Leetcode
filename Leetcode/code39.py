# author : 'wangzhong';
# date: 26/12/2020 02:04

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        def helper(nums, start):
            if target < sum(temp):
                return
            if target == sum(temp):
                ans.append(list(temp))
                return
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                temp.append(nums[i])
                helper(nums, i)
                temp.pop()
        helper(candidates, 0)
        return ans