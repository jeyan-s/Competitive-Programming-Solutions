# Link to Problem Statement
# https://codeforces.com/contest/1884/problem/B

from collections import defaultdict as dd 

for _ in range(int(input())):
  n = int(input())
  string = input()
  rslt = [-1] * n
  cost = 0
  r = 0
  y = 0
  for x in range(n - 1, -1, -1):
    if string[x] == '0':
      rslt[y] = cost 
      cost -= 1 
      y += 1
    cost += 1 
  
  for x in range(1, n):
    if rslt[x] == -1:
      break
    rslt[x] += rslt[x - 1]
    
  print(*rslt)
