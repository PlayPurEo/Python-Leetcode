# author : 'wangzhong';
# date: 14/12/2020 22:47

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            key = "".join(sorted(i))
            ansList = ans.get(key, [])
            ansList.append(i)
            ans[key] = ansList
        return list(ans.values())