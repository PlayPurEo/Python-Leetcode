# author : 'wangzhong';
# date: 22/12/2020 16:31


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        ans = [1, 1]
        for i in range(2, n + 1):
            ans.append(ans[i - 2] + ans[i - 1])
        return ans[-1]