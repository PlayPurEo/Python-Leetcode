# author : 'wangzhong';
# date: 23/12/2020 17:55

"""
给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = chars[0]
        length = 1
        ans = [s]
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if length != 1:
                    for x in str(length):
                        ans.append(x)
                s = chars[i]
                length = 1
                ans.append(s)
            else:
                length += 1
        if length != 1:
            for x in str(length):
                ans.append(x)
        if len(ans) <= len(chars):
            chars = ans[:]
        return len(chars)

    # O（1）空间复杂度
    def compress2(self, chars: List[str]) -> int:
        write = prev = 0
        for i in range(0, len(chars)):
            if i + 1 == len(chars) or chars[i] != chars[i + 1]:
                chars[write] = chars[prev]
                write += 1
                if i > prev:
                    for x in str(i - prev + 1):
                        chars[write] = x
                        write += 1
                prev = i + 1
        return write

if __name__ == '__main__':
    a = [1, 2, 3]
    print(id(a))
    b = [4, 5, 6]
    print(id(b))
    a[:] = b
    print(id(a))
    a = b
    print(id(a))