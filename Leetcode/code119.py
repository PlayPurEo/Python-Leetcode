# author : 'wangzhong';
# date: 10/12/2020 20:27

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
code118
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        finalList = [[1]]
        while len(finalList) <= rowIndex:
            finalList.append([a + b for a, b in zip([0] + finalList[-1], finalList[-1] + [0])])
        return finalList[-1]
