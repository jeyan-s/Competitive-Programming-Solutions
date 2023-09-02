# Link to Problem Statement
# https://codeforces.com/contest/1789/problem/B

def solve():
    n = int(input())
    lst = list(map(int, list(input())))
    x = 0
    found = False
    Break = False
    for x in range(n // 2):
        if lst[x] != lst[n - x - 1]:
            if found and Break:
                return False
            found = True
        else:
            if found:
                Break = True
    return True
    
for x in range(int(input())):
    print("Yes" if solve() else "No")
