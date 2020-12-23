# author : 'wangzhong';
# date: 16/12/2020 13:52

"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ans = {}
        sList = s.split(" ")
        if len(pattern) != len(sList):
            return False
        for i in range(len(sList)):
            if pattern[i] not in ans.keys():
                if sList[i] in ans.values():
                    return False
                ans[pattern[i]] = sList[i]
            else:
                if sList[i] != ans[pattern[i]]:
                    return False
        return True


if __name__ == '__main__':
    s = "a b c"
    print(s.split(" "))