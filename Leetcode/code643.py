# author : 'wangzhong';
# date: 04/02/2021 18:00

"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / len(nums)
        left = 0
        right = k - 1
        sumNumber = 0
        for i in range(k):
            sumNumber += nums[i]
        average = sumNumber / k
        while right < len(nums) - 1:
            sumNumber -= nums[left]
            right += 1
            sumNumber += nums[right]
            average = max(average, sumNumber / k)
            left += 1
        return average