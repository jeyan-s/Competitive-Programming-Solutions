# Link to Problem Statement
# https://codeforces.com/contest/1846/problem/A

for _ in range(int(input())):
    n = int(input())
    lst = [list(map(int, input().split())) for x in range(n)]
    rslt = 0
    for x, y in lst:
        rslt += (x > y)
    print(rslt)
