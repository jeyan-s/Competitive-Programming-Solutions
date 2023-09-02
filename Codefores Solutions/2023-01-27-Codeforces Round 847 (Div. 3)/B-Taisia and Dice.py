# Link to Problem Statement
# https://codeforces.com/contest/1790/problem/B

for _ in range(int(input())):
    n, s, r = map(int, input().split())
    last = s - r
    s -= last
    n -= 1
    lst = [s // n] * n
    rem = s % n
    x = 0
    while rem:
        peak = min(rem, last - lst[x])
        rem -= peak
        lst[x] += peak
        x += 1
    print(*lst, last)
