# Link to Problem Statement
# https://codeforces.com/contest/1809/problem/A
from collections import defaultdict as dd
for _ in range(int(input())):
    string = input().strip()
    Hash = dd(int)
    for x in string:
        Hash[x] += 1
    lst = list(Hash.values())
    lst.sort()
    n = len(Hash)
    if n == 1:
        print(-1)
    elif n == 2:
        if lst[0] == 1:
            print(6)
        else:
            print(4)
    else:
        print(4)
