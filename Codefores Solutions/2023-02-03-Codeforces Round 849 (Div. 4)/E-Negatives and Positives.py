Link to Problem statement
https://codeforces.com/contest/1791/problem/E

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    zero = 0 in lst
    neg = sum(int(x < 0) for x in lst)
    if neg % 2 == 0:
        print(sum(abs(x) for x in lst))
    else:
        if zero:
            print(sum(abs(x) for x in lst))
        else:
            Min = float('inf')
            for x in lst:
                if abs(x) < Min:
                    Min = abs(x)
            print(sum(abs(x) for x in lst) - 2 * Min)
