# author : 'wangzhong';
# date: 05/01/2021 16:07

"""
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for i in range(len(paths)):
            start.add(paths[i][0])
            end.add(paths[i][1])
        return (end - start).pop()