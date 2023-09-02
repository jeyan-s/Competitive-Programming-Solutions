# Link to Problem Statement
# https://codeforces.com/contest/1799/problem/A

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    Set = set()
    rslt = [-1] * n
    y = n - 1
    Time = 1
    for x in lst:
        if y < 0: break
        if x not in Set:
            Set.add(x)
            rslt[y] = Time
            y -= 1
        Time += 1
    print(*rslt)
