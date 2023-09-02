# Link to Problem Statement
# https://codeforces.com/contest/1791/problem/A

string = "codeforces"
for _ in range(int(input())):
    char = input()
    if char in string:
        print("YES")
    else:
        print("NO")
