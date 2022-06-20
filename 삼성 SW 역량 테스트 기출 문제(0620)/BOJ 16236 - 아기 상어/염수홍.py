import sys
sys.stdin = open('input5.txt')
from collections import deque

def check_board(shark):
    for i in range(N):
        for j in range(N):
            if sea[i][j] != 0 and sea[i][j] < shark:
                return True
    return False

def StartBFS():
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:  # 아기상어가 있는 곳에서  start
                sea[i][j] = 0 # 상어 위치에 아무것도 없게 바꿔 줌
                BFS((i, j))
                return

def BFS(point):
    visited = [[0] * N for _ in range(N)]
    di, dj = [-1, 0, 0, 1], [0, -1, 1, 0]  # 거리가 가까운 물고기가 많다면 가장 위 이거랑 상관 있음
    babyshark, cnt = 2, 0
    q = deque()
    visited[point[0]][point[1]] = 1
    q.append(point)
    eat = 0
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0: # 다음 칸이 범위 안에 있을 경우
                if babyshark > sea[ni][nj] and sea[ni][nj] != 0: # 물고기가 상어보다 작다.
                    q = deque()
                    q.append((ni, nj))
                    sea[ni][nj] = 0
                    cnt += visited[row][col]
                    visited = [[0] * N for _ in range(N)] # visited 초기화
                    visited[ni][nj] = 1
                    if eat == babyshark - 1: # 자신과 같은 수의 물고기를 먹을 예정이라면 !
                        eat = 0 # eat 초기화
                        babyshark += 1
                        break
                    else:
                        eat += 1 # eat 올려줌
                        break

                elif sea[ni][nj] == 0 or babyshark == sea[ni][nj]:  # 상어와 같거나 그냥 0이 있는 곳이라면
                    q.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1
                else:
                    pass

    print(cnt)



# 아기상어의 초기 크기는 2, 초기 위치 9 1초에 1칸씩 이동
# babyshark = 2,

# 큰 물고기가 있는 칸은 지날 수 없다.
# if babyshark < sea[ni][nj]

# 작은 물고기는 먹을 수 있다. 지나갈 수 있다.
# if babyshark > sea[ni][nj] , sea[ni][nj] = 0, babyshark += 1

# 크기가 같은 물고기는 먹을 수는 없지만, 지나갈 수 있다
#  if babyshark == sea[ni][nj] 지나가기 가능

# 먹을 수 있는 물고기가 없으면 끝


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

if check_board(2):
    StartBFS()
else:
    print(0)


