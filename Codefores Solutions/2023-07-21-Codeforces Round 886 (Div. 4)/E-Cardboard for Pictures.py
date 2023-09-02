# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/E

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write

for _ in range(int(input())):
  n, c = map(int, input().split())
  lst = list(map(int, input().split()))
  low = 0
  high = 10 ** 9
  tmp = 0
  mid = 1
  for x in range(n):
    t = 2 * mid + lst[x]
    tmp += (t * t)
  # print(mid, t, c)
  # print()
  while low <= high:
    mid = (low + high) // 2
    tmp = 0
    for x in range(n):
      t = 2 * mid + lst[x]
      tmp += (t * t)
    # print(mid, tmp, c)
    if tmp == c:
      print(mid)
      break
    if tmp > c:
      high = mid - 1
    else:
      low = mid + 1
