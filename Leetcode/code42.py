# author : 'wangzhong';
# date: 27/01/2021 15:39

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
解法：按列求
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        sum = 0
        maxLeft = [0] * n
        maxRight = [0] * n
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        for i in range(1, n - 1):
            min_height =  min(maxRight[i], maxLeft[i])
            if min_height > height[i]:
                sum += min_height - height[i]
        return sum