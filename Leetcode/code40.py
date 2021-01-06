# author : 'wangzhong';
# date: 26/12/2020 02:13

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        candidates.sort()
        def helper(nums, start):
            if sum(temp) > target:
                return
            if sum(temp) == target:
                ans.append(list(temp))
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                helper(nums, i + 1)
                temp.pop()
        helper(candidates, 0)
        return ans