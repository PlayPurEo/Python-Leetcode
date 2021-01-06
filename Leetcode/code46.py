# author : 'wangzhong';
# date: 25/12/2020 19:18

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        indexTemp = set()
        def helper(nums: List[int]):
            for i in range(len(nums)):
                if i not in indexTemp:
                    temp.append(nums[i])
                    indexTemp.add(i)
                    if len(temp) == len(nums):
                        ans.append(list(temp))
                        temp.pop()
                        indexTemp.remove(i)
                        break
                    helper(nums)
                    temp.pop()
                    indexTemp.remove(i)
        helper(nums)
        return ans