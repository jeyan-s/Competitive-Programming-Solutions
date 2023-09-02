# Link to Problem Statement
# https://codeforces.com/contest/1844/problem/B


def prime(n):
    n += 1
    lst = [1] * n
    for x in range(2, n):
        if lst[x]:
            for y in range(x * x, n, x):
                lst[y] = False
    lst[0] = lst[1] = False
    return lst
    

primes = prime(2 * 10 ** 5)
# print(primes[:15])

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    rslt = []
    nonprimes = []
    p = []
    l = False
    for x in range(3, 1 + n):
        if not primes[x]:
            # print(x, primes[x])
            nonprimes.append(x)
        else:
            p.append(x)
    one = 1
    p.reverse()
    rslt = nonprimes + p
    # print(nonprimes, p)
    rslt.insert(0, 2)
    rslt.insert(n // 2, 1)
    print(*rslt)
