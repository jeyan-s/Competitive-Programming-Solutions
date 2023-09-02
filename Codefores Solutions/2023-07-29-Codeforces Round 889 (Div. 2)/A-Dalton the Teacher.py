# Link to Problem Statement
# https://codeforces.com/contest/1855/problem/A

from collections import defaultdict as dd
from math import log2, ceil, floor, gcd
from heapq import heapify, heappop, heappush
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left as bst
from bisect import bisect_right as brt

setrecursionlimit(10 ** 8)
input = stdin.readline

for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  rslt = 0
  for x in range(n):
    if x + 1 == lst[x]:
      rslt += 1
  print(ceil(rslt / 2))
