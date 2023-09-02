# Link to problem Statement
# https://codeforces.com/contest/1798/problem/B

from collections import defaultdict as dd

def solve(lst, m):
    rslt = []
    Hash = dd(int)
    for x in lst:
        r = -1
        for y in x:
            if Hash[y] == 0:
                r = y
            Hash[y] += 1
        if r == -1:
            return False
        rslt.append(r)
    rslt.reverse()
    # print(rslt)
    return rslt
    
for _ in range(int(input())):
    m = int(input())
    lst = []
    for __ in range(m):
        n = int(input())
        l = list(map(int, input().split()))
        lst.append(l)
    lst.reverse()
    # print(*lst)
    rslt = solve(lst, m)
    if rslt:
        print(*rslt)
    else:
        print(-1)
