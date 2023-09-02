// Link to Problem Statement
// https://codeforces.com/contest/1864/problem/C

for _ in range(int(input())):
  n = int(input())
  string = bin(n)[2:]
  lst = []
  tmp = n
  pw = 1
  while tmp:
    if tmp & 1:
      lst.append(pw)
    pw *= 2
    tmp //= 2
  if lst[-1] != 1:
    last = lst.pop(-1) // 2
    while last:
      lst.append(last)
      last //= 2
  print(len(lst) + 1)
  print(n, end = ' ')
  for x in lst:
    n -= x
    print(n, end = ' ')
  print()
