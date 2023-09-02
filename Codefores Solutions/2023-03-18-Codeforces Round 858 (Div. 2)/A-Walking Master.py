# Link to Problem Statement
# https://codeforces.com/contest/1806/problem/A

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b > d or a + d - b < c:
        print(-1)
    else:
        rslt = d - b
        rslt += (a + d - b - c)
        print(rslt)
