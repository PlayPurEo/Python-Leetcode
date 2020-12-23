# author : 'wangzhong';
# date: 24/11/2020 21:16

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

解法：滑动窗口
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        max_length = 0
        pointer = -1
        n = len(s)
        for i in range(n):
            # 窗口往前滑动，把滑出去的那个元素从set里去掉
            if i != 0:
                str_set.remove(s[i - 1])
            while pointer + 1 < n and s[pointer + 1] not in str_set:
                str_set.add(s[pointer + 1])
                pointer += 1

            max_length = max(max_length, pointer - i + 1)
        return max_length


if __name__ == '__main__':
    s = "abbdefg"
    solution = Solution()
    max_length = solution.lengthOfLongestSubstring(s)
    print(max_length)