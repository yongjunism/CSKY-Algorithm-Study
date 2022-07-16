import re

string = input()
regex = re.compile('(100+1+|01)+')
matched = regex.fullmatch(string)

if matched:
    print('SUBMARINE')
else:
    print('NOISE')