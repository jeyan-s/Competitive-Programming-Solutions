# Link to Problem Statement
# https://codeforces.com/contest/1878/problem/B

lst = list(range(1, 500001, 2))
for _ in range(int(input())):
  print(*lst[:int(input())])
