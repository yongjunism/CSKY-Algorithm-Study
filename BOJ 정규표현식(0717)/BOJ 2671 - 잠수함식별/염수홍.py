
import re
import sys

sys.stdin = open('input2.txt')

signals = input()
p = re.compile('(100+1+|01)+')
if p.fullmatch(signals):
    print("SUBMARINE")
else:
    print("NOISE")
