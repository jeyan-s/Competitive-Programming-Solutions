# Link to Problem Statement
# https://codeforces.com/contest/1846/problem/B

def solve(field):
    if field[0] == field[1] == field[2] and field[2] != '.':
        return field[0]
    
    if field[3] == field[4] == field[5] and field[5] != '.':
        return field[3]
        
    
    if field[6] == field[7] == field[8] and field[8] != '.':
        return field[6]
        
    if field[0] == field[3] == field[6] and field[6] != '.':
        return field[0]
        
    if field[1] == field[4] == field[7] and field[7] != '.':
        return field[1]
        
    if field[2] == field[5] == field[8] and field[8] != '.':
        return field[2]
        
    if field[0] == field[4] == field[8] and field[8] != '.':
        return field[0]
        
    if field[2] == field[4] == field[6] and field[6] != '.':
        return field[2]
        
    return "DRAW"

for _ in range(int(input())):
    field = [list(input()) for x in range(3)]
    lst = []
    for x in field:
        lst.extend(x)
    print(solve(lst))
