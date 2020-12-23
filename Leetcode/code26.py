# author : 'wangzhong';
# date: 10/12/2020 15:33

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1