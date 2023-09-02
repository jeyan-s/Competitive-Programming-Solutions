# Link to Problem Statement
# https://codeforces.com/contest/1810/problem/B

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
        continue
    if n % 2 == 0:
        print(-1)
        continue
    rslt = []
    n -= 1
    n //= 2
    while n >= 1:
        if n & 1:
            rslt.append(2)
        else:
            rslt.append(1)
        n //= 2
    rslt.reverse()
    print(len(rslt))
    print(*rslt)
