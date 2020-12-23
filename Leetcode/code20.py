# author : 'wangzhong';
# date: 22/12/2020 15:04

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack or pairs[stack.pop()] != ch:
                    return False
        return not stack