# author : 'wangzhong';
# date: 03/03/2021 18:17

# while True:
#     try:
#         str = input()
#         s = ""
#         s = s + (str)
#         last = len(str) % 8
#         if last:
#             for i in range(last, 8):
#                 s = s + '0'
#         start = 0
#         while start < len(s):
#             print(s[start: start + 8])
#             start += 8
#     except:
#         break



# str = input()
# flag = True
# for s in str:
#     if not s.islower() and not s.isupper():
#         print(0)
#         flag = False
#         break
#
# ans = list()
# if flag:
#     for i in range(len(str)):
#         if not ans:
#             ans.append(str[i])
#         else:
#             if str[i] == ans[len(ans) - 1]:
#                 ans.pop()
#             else:
#                 ans.append(str[i])
#     print(len(ans))


# target = input()
# source = input()
# tar_len = len(target)
# sou_len = len(source)
# temp = []
# flag = False
# for i in range(sou_len):
#     temp.append(source[i])
# for i in range(tar_len - 1, -1, -1):
#     while temp[-1] != target[i]:
#         temp.pop()
#     if not temp:
#         break
#     if i == 0 and temp:
#         print(len(temp) - 1)
#         flag = True
#         break
#     if temp and temp[-1] == target[i]:
#         temp.pop()
# if not flag:
#     print(-1)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_pa = self.find(x)
        y_pa = self.find(y)
        if x_pa != y_pa:
            self.parent[x_pa] = self.parent[y_pa]
            self.count[y_pa] += self.count[x_pa]


number = input()
number_list = number.split(" ")
row = int(number_list[0])
column = int(number_list[1])
matrix = [[0 for _ in range(column)] for _ in range(row)]
for i in range(row):
        row_info = input()
        row_list = row_info.split(" ")
        for j in range(column):
            matrix[i][j] = int(row_list[j])
uf = UnionFind(row * column)
for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            continue
        if j < column - 1 and matrix[i][j + 1] == 1:
            uf.union(i * column + j, i * column + j + 1)
        if i < row - 1 and matrix[i + 1][j] == 1:
            uf.union(i * column + j, (i + 1) * column + j)
print(max(uf.count))
