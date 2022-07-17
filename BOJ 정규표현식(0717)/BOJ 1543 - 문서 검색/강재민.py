import re

case = input()
word = input()
p = re.compile(word)
m = p.findall(case)
print(len(m))

