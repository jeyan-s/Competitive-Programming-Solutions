# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/D

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write
# n = int(input())

for _ in range(int(input())):
  n, k = map(int, input().split())
  lst = list(map(int, input().split()))
  lst.sort()
  tmp = []
  cnt = rslt = 0
  for x in range(1, n):
    tmp.append(lst[x] - lst[x - 1])
  for x in tmp:
    if x <= k:
      cnt += 1
    else:
      rslt = max(rslt, cnt)
      cnt = 0
  rslt = max(rslt, cnt)
  rslt += 1
  # print(cnt, rslt)
  print(n - rslt)
  # print()
