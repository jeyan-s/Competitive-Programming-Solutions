# Link to Problem Statement
# https://codeforces.com/contest/1881/problem/A

for _ in range(int(input())):
  n, m = map(int, input().split())
  s1 = input()
  s2 = input()
  rslt = 0
  while s2 not in s1 and n <= m * 10:
    rslt += 1 
    s1 += s1 
    n += n 
  if s2 in s1: print(rslt)
  else: print(-1)
