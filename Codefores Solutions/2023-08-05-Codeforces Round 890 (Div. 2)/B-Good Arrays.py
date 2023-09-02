# Link to Problem Statement
# https://codeforces.com/contest/1856/problem/B

for _ in range(int(input())):
  n = int(input())
  lst = list(map(int, input().split()))
  ones = lst.count(1)
  total = sum(lst)
  
  total -= (n - ones)
  if total >= 2 * ones and n != 1:
    print('YES')
  else:
    print('NO')
