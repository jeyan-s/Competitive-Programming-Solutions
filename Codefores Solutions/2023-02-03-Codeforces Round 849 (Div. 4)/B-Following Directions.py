# Link to Problem Statement:
# https://codeforces.com/contest/1791/problem/B

for _ in range(int(input())):
    x, y = 0, 0
    input()
    string = input()
    for z in string:
        if z == "U":
            y += 1
        elif z == "R":
            x += 1
        elif z == "L":
            x -= 1
        else:
            y -= 1
        # print(x, y)
        if x == 1 and y == 1:
            print("YES")
            break
    else:
        print("NO")
