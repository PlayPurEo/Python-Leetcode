# author : 'wangzhong';
# date: 23/12/2020 00:52

"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
解法：双倍字符串，掐头去尾，查看是否包含原字符串s，如果不是重复构成的，掐头去尾之后不可能包含s
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string = s + s
        return s in string[1:len(string) - 1]