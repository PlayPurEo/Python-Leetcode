# author : 'wangzhong';
# date: 18/12/2020 15:39

"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitMask = 0
        for i in nums:
            bitMask ^= i
        diff = bitMask & (-bitMask)
        x = 0
        for i in nums:
            if i & diff != 0:
                x ^= i
        return [x, bitMask ^ x]