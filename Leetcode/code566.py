# author : 'wangzhong';
# date: 17/02/2021 23:49

"""
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
"""
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r != len(nums) * len(nums[0]) // c:
            return nums
        old_r = len(nums)
        old_c = len(nums[0])
        new_list = [[0] * c for _ in range(r)]
        for i in range(r*c):
            new_list[i // c][i % c] = nums[i // old_c][i % old_c]
        return new_list