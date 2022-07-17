import re
#(100~1~|01)~
case = input()
p = re.compile("(100+1+|01)+")
result = re.fullmatch(p,case)

if result : print('SUBMARINE')
else: print('NOISE')