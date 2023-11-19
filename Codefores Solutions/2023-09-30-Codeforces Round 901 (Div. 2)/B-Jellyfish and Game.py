# Link to Problem Statement
# https://codeforces.com/contest/1875/problem/B

def change(lst1, n, lst2, m):
  Min = min(lst1)
  Max = max(lst2)
  if Max > Min:
    lst2.remove(Max)
    lst2.append(Min)
    lst1.remove(Min)
    lst1.append(Max)
  

for _ in range(int(input())):
  n, m, k = map(int, input().split())
  # Hash = dd(int)
  # rslt = 0
  # n = int(input())
  lst1 = list(map(int, input().split()))
  lst2 = list(map(int, input().split()))
  
  for x in range(min(6, k)):
    if x % 2 == 0:
      change(lst1, n, lst2, m)
    else:
      change(lst2, m, lst1, n)
    # print(lst1)
    k -= 1
    
  if k & 1:
    change(lst1, n, lst2, m)
    
  print(sum(lst1))
