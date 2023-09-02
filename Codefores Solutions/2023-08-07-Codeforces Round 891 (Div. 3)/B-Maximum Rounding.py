# Link to Problem Statement
# https://codeforces.com/contest/1857/problem/B

from collections import defaultdict as dd

for _ in range(int(input())):
  
  n = input()
  lst = ['0'] + list(str(n))
  k = len(lst)
  
  Found = 0
  Zero = k
  
  x = k - 1
  
  while x >= 0:
    t = int(lst[x])
    # print(t, k, x)
    if t >= 5:
      Zero = x
      # print(Zero, x)
      if x - 1 >= 0:
        lst[x - 1] = (int(lst[x - 1]) + 1)
    x -= 1
    
  if Zero != 0:
    for x in range(k):
      if x >= Zero:
        lst[x] = 0
      else:
        lst[x] = int(lst[x]) % 10
    
  while lst and lst[0] == 0:
    lst.pop(0)
  print(*lst, sep = '')
