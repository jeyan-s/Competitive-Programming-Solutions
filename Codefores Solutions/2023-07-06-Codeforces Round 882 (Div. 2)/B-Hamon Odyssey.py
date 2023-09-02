# Link to Problem Statement
# https://codeforces.com/contest/1847/problem/B

def solve(lst, n):
    lst.append(0)
    rslt = 0
    And = lst[0]
    for x in range(n):
        And &= lst[x]
        if And == 0:
            rslt += 1
            And = lst[x + 1]
    return max(rslt, 1)
 
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(solve(lst, n))
