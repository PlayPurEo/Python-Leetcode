# author : 'wangzhong';
# date: 08/12/2020 16:26

"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

解法：回溯算法：尝试失败，回到上一步，并把状态还原
"""
from typing import List


class Solution:
    def backTrack(self, S: str, index: int, ans: List[int]) -> bool:

        if index == len(S):
            return len(ans) >= 3
        currLong = 0
        for i in range(index, len(S)):
            # 0开头，且位数超过2，肯定不是答案，直接break
            if i > index and S[index] == '0':
                break
            currLong = currLong*10 + ord(S[i]) - ord('0')
            # 最大数值
            if currLong > 2**31-1:
                break
                # 如果还没达到至少三个数，或者满足斐波那契
            if len(ans) < 2 or currLong == ans[-1] + ans[-2]:
                ans.append(currLong)
                if self.backTrack(S, i + 1, ans):
                    return True
                ans.pop()
            if len(ans) > 2 and currLong > ans[-1] + ans[-2]:
                break
        return False

    def splitIntoFibonacci(self, S: str) -> List[int]:
        # 存放答案
        ans = list()
        self.backTrack(S, 0, ans)
        return ans

if __name__ == '__main__':
    S = "123456579"
    print(Solution().splitIntoFibonacci(S))