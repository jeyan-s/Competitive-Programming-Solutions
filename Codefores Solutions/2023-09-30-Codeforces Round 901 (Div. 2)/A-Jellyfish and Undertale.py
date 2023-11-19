# Link to Problem Statement
# https://codeforces.com/contest/1875/problem/A

for _ in range(int(input())):
  a, b, n = map(int, input().split())
  # Hash = dd(int)
  # rslt = 0
  # n = int(input())
  # lst1 = list(map(int, input().split()))
  lst = list(map(int, input().split()))
  rslt = b
  b = 1 
  for x in lst:
    b = min(a, b + x)
    rslt += b - 1 
    b = 1
  print(rslt)
