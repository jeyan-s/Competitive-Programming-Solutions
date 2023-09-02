# Link to Problem Statement
# https://codeforces.com/contest/1846/problem/C

def solve(lst, target, index):
    lst.sort()
    # print(lst, target)
    points = 0
    Sum = 0
    penality = 0
    for x in lst:
        if target - x >= 0:
            Sum += x
            penality += Sum
            points += 1
            target -= x
        else:
            break
    return (points, penality, index)

for _ in range(int(input())):
    n, m, h = map(int, input().split())
    lst = [list(map(int, input().split())) for x in range(n)]
    new_list = []
    idx = 0
    for x in lst:
        new_list.append(solve(x, h, idx))
        idx += 1
    new_list.sort(key = lambda x: (-x[0], x[1], x[2]))
    q = 1
    # print(new_list)
    # X, Y = new_list[0], new_list[1]
    for x, y, player in new_list:
        if player == 0:
            print(q)
            break
        q += 1
