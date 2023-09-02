# Link to Problem Statement:
# https://codeforces.com/contest/1791/problem/G1

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    for x in range(1, 1 + n):
        lst[x - 1] += x
    lst.sort()
    # print(lst)
    rslt = x = 0
    while x < n and k - lst[x] >= 0:
        k -= lst[x]
        # print(k)
        x += 1
        rslt += 1
    print(rslt)
    # print()
