# author : 'wangzhong';
# date: 23/12/2020 15:49

"""
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""
        for i in address:
            if i == ".":
                s = s + "[" + i + "]"
            else:
                s += i
        return s