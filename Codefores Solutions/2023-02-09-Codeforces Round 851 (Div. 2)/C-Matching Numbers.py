# Link to Problem Statement
# https://codeforces.com/contest/1788/problem/C

from itertools import permutations as pt
from collections import defaultdict as dd

for _ in range(int(input())):
    n = int(input())
    if (n & 1) ^ 1:
        print("NO")
        continue
    lst = []
    lst.append((n, n + 1))
    Max = 2 * n
    x = n - 2
    y = 2
    Min = 2 * n + 2
    while x > 0:
        lst.append((x, Max - x))
        lst.append((y, Min - y))
        x -= 2
        y += 2
        Max -= 1
        Min += 1
    print("YES")
    for x in lst:
        print(*x)
