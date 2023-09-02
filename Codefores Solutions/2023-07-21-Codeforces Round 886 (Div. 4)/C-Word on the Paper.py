# Link to Problem Statement
# https://codeforces.com/contest/1850/problem/C

from collections import defaultdict as dd
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline
# print = stdout.write
# n = int(input())

for _ in range(int(input())):
  lst = [input() for x in range(8)]
  indx = -1
  Found = False
  for x in range(8):
    for y in range(8):
      if lst[x][y] != '.':
        # print(lst[x][y])
        indx = (x, y)
        Found = True
        break
    if Found: break
  
  if indx == -1:
    print('')
    continue
  x, y = indx
  rslt = ''
  while x < 8 and lst[x][y] != '.':
    rslt += lst[x][y]
    x += 1
  print(rslt)
