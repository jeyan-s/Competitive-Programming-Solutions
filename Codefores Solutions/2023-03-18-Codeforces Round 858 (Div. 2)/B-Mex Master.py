# Link to Problem Statement
# https://codeforces.com/contest/1806/problem/B

from math import ceil
from collections import defaultdict as dd

def Mex(lst, n):
    Hash = dd(int)
    for x in lst:
        Hash[x] += 1
    for x in range(0, n + 1):
        if Hash[x] == 0:
            return x
        
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    zero = 0
    limit = ceil(n / 2)
    for x in lst:
        zero += (x == 0)
    if zero > limit:
        ones = gtr = 0
        for x in lst:
            if x == 1:
                ones += 1
            if x > 1:
                gtr += 1
        if ones and gtr:
            print(1)
        else:
            if ones: print(2)
            else: print(1)
    else:
        print(0)
