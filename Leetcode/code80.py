# author : 'wangzhong';
# date: 10/12/2020 19:27

"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

删除1：code26

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(2, len(nums)):
            if nums[i] > nums[index - 1]:
                index += 1
                nums[index] = nums[i]
        return index + 1
