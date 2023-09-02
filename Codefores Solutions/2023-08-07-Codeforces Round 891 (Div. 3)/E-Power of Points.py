# Link to Problem Statement
# https://codeforces.com/contest/1857/problem/E

from collections import defaultdict as dd

def solve(lst, n, Hash):
  lst.sort(reverse = 1)
  prefix = [0]
  Sum = sum(lst)
  S = Sum
  prefix = 0
    
  for x in range(n):
    t = prefix - (x * lst[x])
    prefix += lst[x]
    t += (n - x) * lst[x] - S
    S -= lst[x]
    Hash[lst[x]] = t + n
  

for _ in range(int(input())):
  
  n = int(input())
  lst = list(map(int, input().split()))
  # Sum = sum(lst)
  
  Sum = sum(lst)
  lst = [(lst[x], x) for x in range(n)]
  Hash = dd(lambda : -1)
  
  # solve(lst.copy(), n, Hash)
  
  lst.sort(reverse = 1)
  prefix = [0]
  S = Sum
  prefix = 0
    
  for x in range(n):
    t = prefix - (x * lst[x][0])
    prefix += lst[x][0]
    t += (n - x) * lst[x][0] - S
    S -= lst[x][0]
    Hash[lst[x]] = t + n
  
  lst.sort(key = lambda x: x[1])
  for x in lst:
    print(Hash[x], end = ' ')
    
  print()
