# author : 'wangzhong';
# date: 21/02/2021 20:55

"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。
"""
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 0
        left = right = 0
        queue_min = deque()
        queue_max = deque()
        while right < n:
            while queue_max and queue_max[-1] < nums[right]:
                queue_max.pop()
            while queue_min and queue_min[-1] > nums[right]:
                queue_min.pop()
            queue_max.append(nums[right])
            queue_min.append(nums[right])
            while queue_min and queue_max and queue_max[0] - queue_min[0] > limit:
                if nums[left] == queue_max[0]:
                    queue_max.popleft()
                if nums[left] == queue_min[0]:
                    queue_min.popleft()
                left += 1
            res = max(res, right + 1 - left)
            right += 1
        return res