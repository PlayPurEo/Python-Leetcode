# author : 'wangzhong';
# date: 18/12/2020 15:12

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans = 0
        # for i in nums:
        #     ans ^= i
        # return ans

        return reduce(lambda x, y: x ^ y, nums)
