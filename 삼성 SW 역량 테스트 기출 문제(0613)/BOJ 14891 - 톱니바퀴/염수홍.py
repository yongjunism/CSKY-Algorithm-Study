import sys
sys.stdin = open('input4.txt')
from collections import deque

def Rotate_R(num, direction):
    if num > 3 or wheels[num - 1][2] == wheels[num][6]: # 내 기준 왼쪽 것과 같은 극이면
        return
    if wheels[num - 1][2] != wheels[num][6]:
        Rotate_R(num + 1, -direction) # 다음거는 반대방향
        wheels[num].rotate(direction) # 나는 기존 방향

def Rotate_L(num, direction):
    if num < 0 or wheels[num][2] == wheels[num + 1][6]:
        return
    if wheels[num + 1][6] != wheels[num][2]:
        Rotate_L(num - 1, -direction)
        wheels[num].rotate(direction)

wheels =[]
for _ in range(4):
    wheel = deque(list(map(int, input().rstrip())))
    wheels.append(wheel)
K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())

    Rotate_R(num + 1 - 1, -direction) # 다음거는 반대방향으로 돌아야 함 / 인덱스 맞춰주기
    Rotate_L(num - 1 - 1, -direction)
    wheels[num - 1].rotate(direction)

ans = 0
for i in range(4): # S극이 1이기 때문에
    ans += wheels[i][0] * (2 ** i)

print(ans)


