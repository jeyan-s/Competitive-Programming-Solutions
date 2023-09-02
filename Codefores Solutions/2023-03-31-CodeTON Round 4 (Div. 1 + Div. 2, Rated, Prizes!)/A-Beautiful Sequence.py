# Link to Problem Statement
# https://codeforces.com/contest/1810/problem/A

t = int(input())
for _ in range(t):
	n = int(input())
	lst = list(map(int, input().split()))
	res = 0
	for i in range(n):
		if(lst[i]-1 <= i):
			res = 1
			break
	if(res == 1):
		print("YES")
	else:
		print("NO")
