# author : 'wangzhong';
# date: 22/02/2021 21:53

"""
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row - 1):
            for j in range(column - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True