import re

t_c = int(input())
answer = []
for _ in range(t_c):
    case = input()
    p = re.compile("[0-9]+")
    m = p.findall(case)
    answer.extend(list(map(int,m)))


answer = sorted(answer)
for i in answer : print(i)