from collections import deque
import sys 
input = sys.stdin.readline

saw = [deque(list(input().rstrip())) for _ in range(4)]
k = int(input())
rotation = [list(map(int, input().split())) for _ in range(k)]


def left_check(num, dir):
    if num < 0:
        return
    if saw[num][2] != saw[num+1][6]:
        left_check(num-1, -dir)
        saw[num].rotate(dir)

def right_check(num, dir):
    if num > 3:
        return
    if saw[num][6] != saw[num-1][2]:
        right_check(num+1, -dir)
        saw[num].rotate(dir)
    
for i in range(k):
    num = rotation[i][0] - 1
    dir = rotation[i][1]
    left_check(num-1, -dir)
    right_check(num+1, -dir)
    saw[num].rotate(dir)

score = 0
for i in range(4):
    if saw[i][0] == '1':
        score += (2**i)
print(score)