# Link to Problem Statement
# https://codeforces.com/contest/1804/problem/A

for _ in range(int(input())):
    a, b = map(int, input().split())
    a = abs(a)
    b = abs(b)
    Min, Max = min(a, b), max(a, b)
    rslt = 2 * Min
    if Max - Min: rslt += (abs(Max - Min) * 2 - 1)
    print(rslt)
