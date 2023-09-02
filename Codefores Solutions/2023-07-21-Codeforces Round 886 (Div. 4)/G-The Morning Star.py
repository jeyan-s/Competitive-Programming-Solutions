# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/G

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write
# n = int(input())

for _ in range(int(input())):
  n = int(input())
  points = [list(map(int, input().split())) for x in range(n)]
  Hash1 = dd(int)
  Hash2 = dd(int)
  Hash3 = dd(int)
  Hash4 = dd(int)
  h = dd(int)
  # points = [(-2, 2), (2, 2)]
  for x, y in points:
    p1 = (x - x, y - x)
    p2 = (x - x, y + x)
    p3 = (x - x, y)
    p4 = (x, y - y)
    st = set([p1, p2, p3, p4])
    # print(p1, p2, p3, p4)
    Hash1[p1] += 1
    Hash2[p2] += 1
    Hash3[p3] += 1
    Hash4[p4] += 1
    for x in st:
      h[x] += 1
  rslt = 0
  # for x in Hash:
  #   rslt += (Hash[x] * (Hash[x] - 1))
  r = 0
  for x in Hash1:
    rslt += (Hash1[x] * (Hash1[x] - 1))
  for x in Hash2:
    rslt += (Hash2[x] * (Hash2[x] - 1))
  for x in Hash3:
    rslt += (Hash3[x] * (Hash3[x] - 1))
  for x in Hash4:
    rslt += (Hash4[x] * (Hash4[x] - 1))
  # print(h)
  print(rslt)
