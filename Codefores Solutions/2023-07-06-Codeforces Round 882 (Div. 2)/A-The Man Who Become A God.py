# Link to Problem Statement
# https://codeforces.com/contest/1847/problem/A

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    new_lst = []
    for x in range(n - 1):
        new_lst.append(abs(lst[x] - lst[x + 1]))
    new_lst.sort()
    print(sum(new_lst[:n - k]))
