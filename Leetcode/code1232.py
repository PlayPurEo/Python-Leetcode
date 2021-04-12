# author : 'wangzhong';
# date: 17/01/2021 14:54

"""
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) == 1:
            return True
        if coordinates[1][0] - coordinates[0][0] != 0:
            gradient = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        else:
            gradient = float('inf')
        for i in range(1, len(coordinates) - 1):
            if coordinates[i+1][0] - coordinates[i][0] != 0:
                temp = (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0])
            else:
                temp = float('inf')
            if temp != gradient:
                return False
        return True