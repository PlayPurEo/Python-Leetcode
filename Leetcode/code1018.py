# author : 'wangzhong';
# date: 14/01/2021 14:13

"""
给定由若干 0 和 1 组成的数组 A。
我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        n = len(A)
        count = 0
        for i in range(n):
            count = count*2 + A[i]
            if count % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans