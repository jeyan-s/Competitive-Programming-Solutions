# Link to Problem Statement
# https://codeforces.com/contest/1791/problem/D

from collections import defaultdict as dd
for _ in range(int(input())):
    n = int(input())
    string = input()
    Hash = dd(int)
    Map = dd(int)
    rslt = 0
    for x in string:
        Hash[x] += 1
    for x in string[:-1]:
        Map[x] += 1
        Hash[x] -= 1
        tmp = 0
        for x in Hash:
            if Hash[x] > 0:
                tmp += 1
        for x in Map:
            if Map[x] > 0:
                tmp += 1
        rslt = max(rslt, tmp)
    print(rslt)
