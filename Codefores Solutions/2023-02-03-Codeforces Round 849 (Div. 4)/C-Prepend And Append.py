# Link to Problem Statement
# https://codeforces.com/contest/1791/problem/C

for _ in range(int(input())):
    n = int(input())
    string = input()
    low = 0
    high = n - 1
    while (low < high):
        if string[low] == string[high]:
            break
        low += 1
        high -= 1
    print(high - low + 1)
