# author : 'wangzhong';
# date: 31/01/2021 17:07

"""
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
"""
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def check(a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret