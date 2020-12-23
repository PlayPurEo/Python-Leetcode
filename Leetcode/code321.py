# author : 'wangzhong';
# date: 20/12/2020 15:41

"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。
"""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 该步骤同code402
        def pickMax(num: List[int], k):
            stack = []
            length = len(num) - k
            for i in num:
                while length and stack and stack[-1] > i:
                    stack.pop()
                    length -= 1
                stack.append(i)
            return stack[:k]
        def merge(nums1: List[int], nums2: List[int]):
            ans = []
            while nums1 and nums2:
                if nums1[0] >= nums2[0]:
                    ans.append(nums1[0])
                    nums1.pop(0)
                else:
                    ans.append(nums2[0])
                    nums2.pop(0)
            if nums1:
                ans += nums1
            else:
                ans += nums2
            return ans

        return max(merge(pickMax(nums1, i), pickMax(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))