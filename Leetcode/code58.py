# author : 'wangzhong';
# date: 22/12/2020 00:18

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split(" ")
        for i in range(len(ans) - 1, -1, -1):
            if ans[i]:
                return len(ans[i])
        return 0


if __name__ == '__main__':
    a = " "
    ans = a.split(" ")
    for i in range(len(ans) - 1, -1, -1):
        if ans[i]:
            print(ans[i])