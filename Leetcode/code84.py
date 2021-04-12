# author : 'wangzhong';
# date: 08/01/2021 12:49

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        ans = 0
        queue = deque()
        for i in range(n):
            # 前面高的可以弹出计算面积
            while queue and heights[queue[-1]] > heights[i]:
                height = heights[queue.pop()]
                # 去掉同等高度的
                while queue and heights[queue[-1]] == height:
                    queue.pop()
                # 计算宽度
                if not queue:
                    width = i
                else:
                    width = i - queue[-1] - 1
                ans = max(ans, width * height)
            queue.append(i)
        while queue:
            height = heights[queue.pop()]
            # 去掉同等高度的
            while queue and heights[queue[-1]] == height:
                queue.pop()
            # 计算宽度
            if not queue:
                width = n
            else:
                width = n - queue[-1] - 1
            ans = max(ans, width * height)
        return ans


if __name__ == '__main__':
    queue = deque()
    queue.append(5)
    queue.pop()
    print(queue)