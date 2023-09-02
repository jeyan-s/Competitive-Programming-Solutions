# Link to Problem Statement
# https://codeforces.com/contest/1851/problem/A

from collections import defaultdict as dd
from sys import setrecursionlimit as st
from sys import stdin, stdout
from heapq import heapify, heappush, heappop

input = stdin.readline
st(10 ** 8)

for _ in range(int(input())):
  # n = int(input())
  # lst = list(map(int, input().split()))
  
  n, m, k, h = map(int, input().split())
  lst = list(map(int, input().split()))
  rslt = 0
  
  for x in range(n):
    for z in range(m):
      my_height = h + z * k
      Found = False
      for y in range(m):
        if z == y: continue
        # print()
        height = y * k + lst[x]
        if height == my_height:
          rslt += 1
          Found = True
          break
      if Found:
        # print(9)
        break
      
  print(rslt)
