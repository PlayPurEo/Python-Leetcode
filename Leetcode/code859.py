# author : 'wangzhong';
# date: 23/12/2020 17:16


"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        # 字符串相等的情况
        if A == B:
            seen = set()
            for i in A:
                if i in seen:
                    return True
                seen.add(i)
            return False
        else:
            first = -1
            second = -1
            for i in range(len(A)):
                if A[i] != B[i]:
                    if first == -1:
                        first = i
                    elif second == -1:
                        second = i
                    else:
                        return False
            return second != -1 and A[first] == B[second] and A[second] == B[first]