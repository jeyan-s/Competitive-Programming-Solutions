# Link to Problem Statement
# https://codeforces.com/contest/1857/problem/A

for _ in range(int(input())):
  
  n = int(input())
  lst = list(map(int, input().split()))
  if sum(lst) & 1:
    print('NO')
  else:
    print('YES')
