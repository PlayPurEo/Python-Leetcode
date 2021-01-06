# author : 'wangzhong';
# date: 05/01/2021 16:22

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        temp = []

        def helper(start: int):
            if start > 9:
                return
            if sum(temp) == n and len(temp) == k:
                ans.append(list(temp))
                return
            if sum(temp) >= n or len(temp) >= k:
                return
            for i in range(start, 10):
                temp.append(i)
                helper(i+1)
                temp.pop()
        helper(1)
        return ans