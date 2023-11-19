# Link to Problem Statement
# https://codeforces.com/contest/1878/problem/B

from math import log, ceil, floor, sqrt, gcd
from heapq import heapify, heappop, heappush
from sys import setrecursionlimit 
from bisect import bisect_left as bst 
from bisect import bisect_right as brt 
from collections import defaultdict as dd 

def dist(x1, y1, x2, y2):
   rslt = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
   return rslt

def contains(x1, y1, x2, y2, r):
  if dist(x1, y1, x2, y2) <= r: return True
  return False
  
def intersects(x1, y1, x2, y2, r):
  return dist(x1, y1, x2, y2) <= r 
  
def solve(ox, oy, px, py, ax, ay, bx, by, mid):
  if contains(ax, ay, px, py, mid) and contains(bx, by, ox, oy, mid) and intersects(ax, ay, bx, by, mid + mid):
    return True
  if contains(bx, by, px, py, mid) and contains(ax, ay, ox, oy, mid) and intersects(ax, ay, bx, by, mid + mid):
    return True
  if contains(ax, ay, px, py, mid) and contains(ax, ay, ox, oy, mid):
    return True
  if contains(bx, by, px, py, mid) and contains(bx, by, ox, oy, mid):
    return True
  return False
    
for _ in range(int(input())):
  ox, oy = 0, 0
  px, py = map(int, input().split())
  ax, ay = map(int, input().split())
  bx, by = map(int, input().split())
  # n = int(input())
  # lst = list(map(int, input().split()))
  # string = input()
  # Hash = dd(int)
  # Set = set()
  low = 0
  high = 10 ** 9
  
  while low < high and high - low > 10 ** (-7):
    mid = low + (high - low) / 2 
    if solve(ox, oy, px, py, ax, ay, bx, by, mid):
      rslt = mid
      high = mid 
    else:
      low = mid
      
  print(rslt)
