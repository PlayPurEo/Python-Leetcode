# author : 'wangzhong';
# date: 06/12/2020 16:36
from typing import List

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        finalList = [[1]]
        while len(finalList) < numRows:
            finalList.append([a + b for a, b in zip([0] + finalList[-1], finalList[-1] + [0])])
        return finalList


if __name__ == '__main__':
    print(Solution().generate(5))
