from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
rotation = []
for _ in range(l):
    x, c = map(str, input().split())
    rotation.append((int(x), c))

dir = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서 순서로 idx와 매칭

def rotate(c):
    global idx
    if c == 'L': # 왼쪽 회전
        if idx != 0: # 서 -> 남 -> 동 -> 북
            idx -= 1
        else:
            idx = 3
    else: # 오른쪽 회전
        if idx != 3: # # 북 -> 동 -> 남 -> 서
            idx += 1
        else:
            idx = 0
    return

snake = deque()
snake.append((0,0))
idx = 1 # 첫 시작 방향 동쪽
x, y, time, init = 0, 0, 0, 1 # 위치, 총 시간, 방향 바꿀 때 시간
flag = False

for i in range(len(rotation)):
    init = time + 1
    for _ in range(init, rotation[i][0] + 1):
        dx, dy = dir[idx][0], dir[idx][1]
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in snake: # 벽 또는 자기 몸통
            time += 1
            flag = True
            break
        
        if board[nx][ny] == 1: # 사과 겟
            board[nx][ny] = 0
            x, y = nx, ny
            snake.append((x,y))
        else:
            x, y = nx, ny
            snake.popleft()
            snake.append((x,y))
        time += 1
    if flag == True:
        break
    rotate(rotation[i][1])
        
print(time)

