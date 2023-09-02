# Link to Problem Statement
# https://codeforces.com/contest/1790/problem/A

pi = "314159265358979323846264338327950288419716939937510 5820974944 5923078164 0628620899 8628034825 3421170679"
for _ in range(int(input())):
    string = input()
    n = len(string)
    rslt = 0
    for x in range(n):
        if string[x] == pi[x]:
            rslt += 1
        else:
            break
    print(rslt)
