# Link to Problem Statement
# https://codeforces.com/contest/1886/problem/B

for _ in range(int(input())):
  # n, k = map(int, input().split())
  n = int(input())
  # lst = list(map(int, input().split()))
  # string = input()
  # Hash = dd(int)
  # Set = set()
  no = "NO"
  yes = "YES"
  if n < 7:
    print(no)
    continue
  if n % 3 == 0:
    if n - 5 != 1 and n - 5 != 4:
      print(yes)
      print(1, 4, n - 5)
    else:
      print(no)
  else:
    if n - 3 > 3:
      print(yes)
      print(1, 2, n - 3)
    else:
      print(no)
    
