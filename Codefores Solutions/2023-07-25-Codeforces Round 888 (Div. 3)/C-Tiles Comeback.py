# Link to Problem Statement
# https://codeforces.com/contest/1851/problem/C

from collections import defaultdict as dd
from sys import setrecursionlimit as st
from sys import stdin, stdout
from heapq import heapify, heappush, heappop

input = stdin.readline
st(10 ** 8)

def solve():
  n, k = map(int, input().split())
  lst = list(map(int, input().split()))
  no = 'NO'
  yes = 'YES'
  # rslt = 0
  
  if lst[0] == lst[-1]:
    if lst.count(lst[0]) >= k:
      return yes
    return no
  
  start = None
  count = 0
  Found = False
  
  for x in range(n):
    if lst[x] == lst[0]:
      start = x
      count += 1
      if count == k:
        Found = True
        break
      
  # print(start, Found, count)
  if not Found: 
    return no
  
  end = None
  count = 0
  Found = False
  
  for x in range(n - 1, -1, -1):
    if lst[x] == lst[n - 1]:
      end = x
      count += 1
      if count == k:
        Found = True
        break
      
  # print(end)
  if not Found: return no
  
  if start < end: return yes
  return no

for _ in range(int(input())):
  print(solve())
  # n = int(input())
  # lst = list(map(int, input().split()))
  
  
