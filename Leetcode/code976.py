# author : 'wangzhong';
# date: 29/11/2020 22:17

"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

贪心+排序
"""
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        A.sort(reverse=True)
        for i in range(0, len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return sum(A[i:i + 3])
        return 0


if __name__ == '__main__':
    s = [3, 2, 3, 4]
    num = Solution().largestPerimeter(s)
    print(num)