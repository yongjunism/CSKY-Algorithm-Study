import sys
sys.stdin = open('input3.txt')
from itertools import permutations


def Calculate(per):
    global max_num, min_num
    answer = nums[0] # 슬라이싱으로 깊은 복사 해옴
    for i in range(len(per)):
        if per[i] == 0:
            answer += nums[i+1]
        elif per[i] == 1:
            answer -= nums[i+1]
        elif per[i] == 2:
            answer *= nums[i+1]
        elif per[i] == 3:
            if answer >= 0:
                answer //= nums[i+1]
            else:
                answer = (-answer // nums[i+1]) * -1
    if answer > max_num:
        max_num = answer
    if answer < min_num:
        min_num = answer
    # result.append(answer)

input = sys.stdin.readline
N = int(input()) # 수의 개수
nums = list(map(int, input().split())) # 숫자들
calculations = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈 개수
new = []
result = []
max_num, min_num = 0, 100000000
for i in range(4): # 0, 1, 2, 3 / 덧셈, 뺄셈, 곱셈, 나눗셈
    for _ in range(calculations[i]):
        new.append(i)

permu = list(permutations(new, len(new)))

for per in permu:
    Calculate(per)
print(max_num)
print(min_num)
# print(result)
# print(max(set(result)))
# print(min(set(result)))