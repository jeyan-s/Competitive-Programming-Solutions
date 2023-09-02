# Link to Problem Statement
# https://codeforces.com/contest/1846/problem/D

rslt = 0
for _ in range(int(input())):
    n, b, h = map(int, input().split())
    lst = list(map(int, input().split()))
    rslt = 0.5 * b * h
    max_height = lst[0] + h
    left = b / 2
    for x in range(1, n):
        cur_base = lst[x]
        dif_height = max_height - cur_base
        if dif_height > 0:
            dif_base = left / h
            dif_base *= dif_height
            dif_base *= 2
            rslt -= (0.5 * dif_base * dif_height)
        rslt += (0.5 * b * h)
        max_height = lst[x] + h
    print(rslt)
            
            
            # (lst[x] - lst[x - 1])
