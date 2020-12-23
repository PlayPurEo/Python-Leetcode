# author : 'wangzhong';
# date: 16/12/2020 14:01

"""
初始时有 n 个灯泡关闭。

第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。

第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。

找出 n 轮后有多少个亮着的灯泡。

解法：如果要亮着，必须有奇数个约数，如果要有奇数个约数，其中两个约数必然相等，因此它是某一个约数的平方！
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        result = 1
        while result*result <= n:
            result += 1
        return result - 1

if __name__ == '__main__':
    print(Solution().bulbSwitch(3))