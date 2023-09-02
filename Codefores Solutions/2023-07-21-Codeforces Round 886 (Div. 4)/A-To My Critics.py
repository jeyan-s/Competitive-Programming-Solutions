# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/A

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write

for _ in range(int(input())):
  # n = int(input())
  a, b, c = map(int, input().split())
  if a + b >= 10 or b + c > 9 or a + c > 9:
    print('YES')
  else:
    print('NO')
  # lst = list(map(int, input().split()))
