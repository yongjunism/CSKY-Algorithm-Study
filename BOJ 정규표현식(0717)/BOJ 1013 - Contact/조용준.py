import sys, re
input = sys.stdin.readline

t = int(input())
radios = [input().rstrip() for _ in range(t)]
p = re.compile('(100+1+|01)+')

for radio in radios:
    if p.fullmatch(radio):
        print('YES')
    else:
        print('NO')
