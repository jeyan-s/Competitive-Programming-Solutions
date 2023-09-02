# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/B

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write
# n = int(input())

for _ in range(int(input())):
  n = int(input())
  cnt = 0
  rslt = -1
  q = 0
  for x in range(n):
    cnt += 1
    n, k = map(int, input().split())
    if n > 10: continue
    if q < k:
      rslt = cnt
      q = k
  print(rslt)
  # lst = list(map(int, input().split()))
