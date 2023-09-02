# Link to Problem Statement
# https://codeforces.com/contest/1857/problem/D

for _ in range(int(input())):
  n = int(input())
  lst1 = list(map(int, input().split()))
  lst2 = list(map(int, input().split()))
  lst = [lst1[x] - lst2[x] for x in range(n)]
  Strong = max(lst)
  rslt = []
  
  for x in range(n):
    if lst[x] >= Strong:
      rslt.append(x + 1)
  
  print(len(rslt))
  print(*rslt)
