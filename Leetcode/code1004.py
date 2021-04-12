# author : 'wangzhong';
# date: 19/02/2021 17:57

"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。
"""
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = right = 0
        zero = 0
        res = 0
        while right < n:
            if A[right] == 0:
                zero += 1
            if zero > K:
                if A[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res