# Link to Problem Statement
# https://codeforces.com/contest/1881/problem/B

def solve1(a, b, c):
  if c == 2 * a or c == 3 * a or c == 4 * a or a == 2 * c:
    return True
  return False
  
def solve2(a, b, c):
  if (a == 2 * c and b == 3 * c):
    return True

for _ in range(int(input())):
  
  a, b, c = map(int, input().split())
  rslt = False
  
  if a == b and b == c:
    print("YES")
    continue
  
  if a == b or b == c or a == c:
    if a == b:
      if a == 2 * c or c == 2 * a or c == 3 * a or c == 4 * a:
        rslt = True
    elif a == c:
      c = b
      if a == 2 * c or c == 2 * a or c == 3 * a or c == 4 * a:
        rslt = True
    elif b == c:
      c = a 
      a = b 
      if a == 2 * c or c == 2 * a or c == 3 * a or c == 4 * a:
        rslt = True
    # rslt = solve1(a, b, c) or solve1(a, c, b) or solve1(b, c, a) or solve1(b, a, c)
    # rslt = rslt or solve1(c, b, a) or solve1(c, a, b)
  else:
    rslt = solve2(a, b, c) or solve2(a, c, b) or solve2(b, c, a) or solve2(b, a, c)
    rslt = rslt or solve2(c, b, a) or solve2(c, a, b)
  
  if rslt:
    print("YES")
  else:
    print("NO")
