# Link to Problem Statement
# https://codeforces.com/contest/1884/problem/A

from collections import defaultdict as dd 

def solve(n, k):
  return sum(map(int, list(str(n)))) % k == 0

for _ in range(int(input())):
  n, k = map(int, input().split())
  while not solve(n, k):
    n += 1 
  print(n)
