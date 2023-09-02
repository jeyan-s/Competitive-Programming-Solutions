# Link to Problem Statement
# https://codeforces.com/contest/1804/problem/B

for _ in range(int(input())):
    n, k, d, w = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    Open = float('-inf')
    Dose = k
    rslt = 0
    y = 1
    for x in lst:
        # if _ + 1 == 2:
        #         print(Open, Dose, Open + d, x)
        if Open + d >= x and Dose > 0:
            Dose -= 1
        else:
            # if y == 1: print(_ + 1)
            rslt += 1
            Open = x + w
            Dose = k - 1
        y += 1
    print(rslt)
