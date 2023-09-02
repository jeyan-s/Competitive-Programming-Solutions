# Link to Problem Statement
# https://codeforces.com/contest/1856/problem/A

from collections import defaultdict as dd
from heapq import heapify, heappop, heappush
from bisect import bisect_right as brt
from bisect import bisect_left as bst
from sys import setrecursionlimit as st
st(10 ** 8)

def valid(lst, n):
  Error = False
  for x in range(1, n):
    if lst[x] < lst[x - 1]:
      Error = True
      break
  return Error
  
def solve(lst, n, d):
  for x in range(n):
    lst[x] -= d
    lst[x] = max(lst[x], 0)
  
for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  rslt = 0
  
  while valid(lst, n):
      # print(lst)
      Min = 10 ** 10
      for x in lst:
        if x != 0: Min = min(Min, x)
      # print(Min)
      rslt += Min
      # print(rslt)
      solve(lst, n, Min)
    
  print(rslt)
