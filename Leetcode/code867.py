# author : 'wangzhong';
# date: 25/02/2021 13:13

"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        new_ma = [[0 for _ in range(row)] for _ in range(column)]
        for j in range(column):
            for i in range(row):
                new_ma[j][i] = matrix[i][j]
        return new_ma