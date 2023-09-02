# Link to Problem Statement
# https://codeforces.com/contest/1853/problem/A

for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  mir = sorted(lst)
  rslt = float('inf')
  if lst == mir:
    for x in range(1, n):
      diff = lst[x] - lst[x - 1]
      rslt = min(diff // 2 + 1, rslt)
  else: rslt = 0
  print(rslt)
