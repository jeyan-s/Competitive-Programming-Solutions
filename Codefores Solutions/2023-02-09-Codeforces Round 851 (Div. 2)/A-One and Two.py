# Link to Problem Statement
# https://codeforces.com/contest/1788/problem/A

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    X = 1
    Y = 1
    found = False
    for x in lst:
        X *= x
    for x in range(n - 1):
        Y *= lst[x]
        if Y == X // Y and not X % Y:
            print(x + 1)
            found = True
            break
    if not found:
        print(-1)
