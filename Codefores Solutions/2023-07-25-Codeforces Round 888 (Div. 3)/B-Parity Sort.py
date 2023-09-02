# Link to Problem Statement
# https://codeforces.com/contest/1851/problem/B

from collections import defaultdict as dd
from sys import setrecursionlimit as st
from sys import stdin, stdout
from heapq import heapify, heappush, heappop

input = stdin.readline
st(10 ** 8)

for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  
  # n, m, k, h = map(int, input().split())
  # lst = list(map(int, input().split()))
  # rslt = 0
  
  odd = []
  eve = []
  o = e = 0
  
  for x in range(n):
    if lst[x] & 1:
      odd.append(lst[x])
    else:
      eve.append(lst[x])
      
  odd.sort()
  eve.sort()
  
  for x in range(n):
    if lst[x] & 1:
      lst[x] = odd[o]
      o += 1
    else:
      lst[x] = eve[e]
      e += 1
      
  Error = 0
  prev = lst[0]
  
  for x in range(1, n):
    if prev > lst[x]:
      Error = True
      break
    prev = lst[x]
    
  if Error: print('NO')
  else: print('YES')
