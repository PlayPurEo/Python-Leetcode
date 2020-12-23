# author : 'wangzhong';
# date: 15/12/2020 12:57

"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
解法：贪心算法
"""

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strN = str(N)
        if len(strN) < 2:
            return N
        c = [int(i) for i in strN]
        i = 1
        while i < len(strN) and strN[i] >= strN[i - 1]:
            i += 1

        while 0 < i < len(strN) and c[i] < c[i - 1]:
            c[i - 1] -= 1
            i -= 1
        i += 1
        for j in range(i, len(strN)):
            c[j] = 9
        return int("".join(list(map(str, c))))

if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(332))
