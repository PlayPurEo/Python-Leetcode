# author : 'wangzhong';
# date: 22/01/2021 13:45

"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        carry = 0
        for i in range(n - 1, -1, -1):
            if K == 0 and carry == 0:
                break
            num = K % 10
            add = A[i] + num + carry
            carry = add // 10
            A[i] = add % 10
            K = K // 10
        while K != 0:
            num = K % 10
            add = num + carry
            carry = add // 10
            A.insert(0, add % 10)
            K = K // 10
        if carry != 0:
            A.insert(0, carry)
        return A