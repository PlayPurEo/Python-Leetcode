# author : 'wangzhong';
# date: 10/12/2020 15:09

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        def threeSum(first: int):
            smallTarget = target - nums[first]
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                    break
                forth = n - 1
                for three in range(second + 1, n - 1):
                    if three > second + 1 and nums[three] == nums[three - 1]:
                        continue
                    while three < forth and nums[second] + nums[three] + nums[forth] > smallTarget:
                        forth -= 1
                    if three == forth:
                        break
                    if nums[second] + nums[three] + nums[forth] == smallTarget:
                        ans.append([nums[first], nums[second], nums[three], nums[forth]])
        for first in range(n - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
                break
            threeSum(first)
        return ans