import re

#(100+1+ | 01)+

t_c = int(input())

for _ in range(t_c) :
    case = input()
    
    p = re.compile('(100+1+|01)+')
    result = re.fullmatch(p,case)
    
    if result:
        print('YES')
    else: print('NO')