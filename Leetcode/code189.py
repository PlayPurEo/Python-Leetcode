# author : 'wangzhong';
# date: 08/01/2021 12:39

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]