# author : 'wangzhong';
# date: 19/12/2020 19:08

"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
自己的想法：由外向内，依次旋转
解法1：找到旋转后对应位置改变的规律：matrix[row][col] = matrix[col][n-1-row]
对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。
解法2：水平反转，再主对角线反转
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def helper(matrix: List[List[int]], start: int, end: int):
            if end <= start:
                return
            temp = matrix[start][start: end + 1]
            for i in range(start, end + 1):
                matrix[start][i] = matrix[end - i + start][start]
            for i in range(start, end + 1):
                matrix[i][start] = matrix[end][i]
            for i in range(start, end + 1):
                matrix[end][i] = matrix[end - i + start][end]
            for i in range(start, end + 1):
                matrix[i][end] = temp[i - start]
            return helper(matrix, start + 1, end - 1)
        helper(matrix, 0, len(matrix[0]) - 1)

    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        newMatrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                newMatrix[j][n - 1 - i] = matrix[i][j]
        matrix[:] = newMatrix


if __name__ == '__main__':
    a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(a)