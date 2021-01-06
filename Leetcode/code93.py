# author : 'wangzhong';
# date: 23/12/2020 16:02

"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，
但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
解法：回溯
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp = []
        ans = []

        def dfs(temp: List[str], start: int):
            # 如果存放了4个ip段且长度用完，添加到结果中
            if len(temp) == 4 and start == len(s):
                ans.append(".".join(temp))
            # 如果没用完，回溯
            if len(temp) == 4 and start < len(s):
                return
            for length in range(1, 4):
                # 如果超过长度，回溯
                if start + length - 1 >= len(s):
                    return
                # 如果0打头且不为0，回溯
                if length != 1 and s[start] == "0":
                    return
                # 如果ip超过255，回溯
                if int(s[start: start + length]) > 255:
                    return
                temp.append(s[start: start + length])
                dfs(temp, start + length)
                # 这个情况走完，要把这次的ip去掉
                temp.pop()
        dfs(temp, 0)
        return ans