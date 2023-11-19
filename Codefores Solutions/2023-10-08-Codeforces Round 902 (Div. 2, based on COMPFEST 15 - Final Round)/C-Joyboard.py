# Link to Problem Statement
# https://codeforces.com/contest/1877/problem/B

for _ in range(int(input())):
  n, m, k = list(map(int, input().split()))
  if k > 3: 
    print(0)
    continue
  if k == 1: 
    print(1) 
    continue
  if k == 3 and m >= n: 
    print(((m + 1) - (n + (m // n))))
    continue
  elif k == 3: 
    print(0)
    continue
  if k == 2: 
    print(min(n - 1, m) + (m // n))
    continue
