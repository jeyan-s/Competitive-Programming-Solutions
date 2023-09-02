# Link to Problem Statement
# https://codeforces.com/contest/1851/problem/D

from collections import defaultdict as dd
from sys import setrecursionlimit as st
from sys import stdin, stdout
from heapq import heapify, heappush, heappop

input = stdin.readline
st(10 ** 8)

for _ in range(int(input())):
  
  n = int(input())
  correct = (n * (n + 1)) // 2
  lst = [0] + list(map(int, input().split())) + [correct]
  new_lst = [lst[x] - lst[x - 1] for x in range(1, n)]
  Hash = dd(int)
  taken = dd(bool)
  another = []
  miss = 0
  l = []
  
  for x in new_lst:
    Hash[x] += 1
    
  for x in range(1, n + 1):
    if Hash[x] == 0:
      miss += 1
      l.append(x)
      
  for x in range(1, n + 1):
    if Hash[x] > 0:
      taken[x] = True
      
  for x in new_lst:
    if taken[x]:
      taken[x] = False
      continue
    if not taken[x]:
      another.append(x)
      
  # print(miss, l, Hash)
  
  if miss > 2:
    print('NO')
    continue
  
  if miss == 1:
    print('YES')
    
  if miss == 2:
    # print(l)
    if sum(l) in another:
      print('YES')
      continue
    print('NO')
