# author : 'wangzhong';
# date: 13/12/2020 13:48

"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
            if hashMap[nums[i]] > 1:
                return True
        return False