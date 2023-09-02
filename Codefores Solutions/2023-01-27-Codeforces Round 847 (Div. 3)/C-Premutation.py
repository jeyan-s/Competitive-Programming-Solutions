# Link to Problem Statement
# https://codeforces.com/contest/1790/problem/C

from collections import defaultdict as dd

for _ in range(int(input())):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    dk = dd(int)
    for x in range(n):
        dk[lst[x][0]] += 1
    first_ = None
    mx = -1
    for x in dk:
        if mx < dk[x]:
            mx = dk[x]
            first_ = x
    rslt = None
    first = None
    for x in lst:
        if x[0] != first_:
            first = x[0]
            rslt = x
            break
    print(first_, *rslt)
