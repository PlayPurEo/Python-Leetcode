# author : 'wangzhong';
# date: 20/12/2020 14:31

"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
解法：贪心+栈
优化：一个数是否在栈内，时间复杂度是O（N），用set时间复杂度是O(1)，因为内部实现是dict
"""
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        strCounter = collections.Counter(s)
        for i in s:
            if i not in seen:
                while stack and stack[-1] > i and strCounter[stack[-1]] > 0:
                    seen.discard(stack.pop(-1))
                seen.add(i)
                stack.append(i)
            strCounter[i] -= 1
        return "".join(stack)


if __name__ == '__main__':
    a = [1,2,3]
    print(str(a))