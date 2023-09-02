# Link to Problem Statement
# https://codeforces.com/contest/1798/problem/A

def solve(lst1, lst2, n):
    an = lst1[-1]
    bn = lst2[-1]
    for X in range(n - 1):
        x = lst1[X]
        y = lst2[X]
        if x > an and x > bn:
            return False
        if y > an and y > bn:
            return False
        if y <= an and x > an or x <= bn and y > bn:
            lst1[X] = y
            lst2[X] = x
        
    # print(lst1, lst2)
    return max(lst1) == an and max(lst2) == bn

for _ in range(int(input())):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    if solve(lst1, lst2, n):
        print("YES")
    else:
        print("NO")
