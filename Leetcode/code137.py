# author : 'wangzhong';
# date: 18/12/2020 15:34

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
解法: ~ & ^
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0
        for i in nums:
            once = ~twice & (once ^ i)
            twice = ~once & (twice ^ i)
        return once