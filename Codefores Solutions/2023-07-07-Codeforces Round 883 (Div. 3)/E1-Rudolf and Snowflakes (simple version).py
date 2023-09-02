# Link to Problem Statement
# https://codeforces.com/contest/1846/problem/E1

from math import log2
from collections import defaultdict as dd

Hash = dd(bool)
for x in range(2, 1001):
    value = 1 + x + x * x
    power = x * x
    while value <= 1000000:
        Hash[value] = True
        power *= x
        value += power

for _ in range(int(input())):
    n = int(input())
    if Hash[n]:
        print('YES')
    else:
        print('NO')
