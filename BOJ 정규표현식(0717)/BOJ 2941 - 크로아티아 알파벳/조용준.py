# 구현
word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = []

for i in croatia:
    cnt.append(word.count(i))
print(len(word) - sum(cnt))

# 정규표현식
import re
print(len(re.sub('c=|c-|dz=|d-|lj|nj|s=|z=', '0', input())))