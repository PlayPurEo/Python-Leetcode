# author : 'wangzhong';
# date: 10/12/2020 16:18

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗

logn就是分治
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]


        def binarySearch() -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid
                else:
                    right = mid - 1
            if nums[left] == target:
                return left
            return -1


        def binarySearchRight() -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                # 向上取整
                mid = (left + right + 1) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    left = mid
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            return -1
        left = binarySearch()
        if left == -1:
            return [-1, -1]
        right = binarySearchRight()
        return [left, right]