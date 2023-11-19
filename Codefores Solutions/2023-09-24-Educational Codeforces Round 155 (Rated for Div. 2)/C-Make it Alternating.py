# Link to Problem Statement
# https://codeforces.com/contest/1879/problem/C

from collections import defaultdict as dd 
from math import ceil, floor, gcd, sqrt, log 
from heapq import heapify, heappop, heappush
from sys import setrecursionlimit 
from bisect import bisect_left as bst 
from bisect import bisect_right as brt 

f = int(3e5)
mod = 998244353
fact = [1] * (f)

for x in range(2, f):
  fact[x] = (fact[x - 1] * (x % mod)) % mod

for _ in range(int(input())):
  
  string = input().strip()
  lst = []
  cnt = 0
  mul = 1 
  rslt = 0
  prev = -1
  for x in string:
    if x != prev and cnt:
      lst.append(cnt)
      mul *= cnt 
      rslt += cnt - 1 
      cnt = 0
    prev = x 
    cnt += 1
  lst.append(cnt)
  mul *= cnt
  rslt += cnt - 1
  # print(rslt, mul, lst)
  print(rslt, (mul * (fact[rslt])) % mod)
