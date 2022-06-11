import sys
sys.stdin = open('input3.txt')
from collections import deque

def findStart():
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                startpoint.append((i, j))

def makeWall(cnt):
    if cnt == 3:
        for start in startpoint:
            q.append(start)
        BFS()
    else:
        for i in range(N):
            for j in range(M):
                if wall_visited[i][j] == 0 and maps[i][j] == 0:
                    wall_visited[i][j] = 1
                    makeWall(cnt + 1)
                    wall_visited[i][j] = 0

def BFS():
    global max_cnt
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and maps[ni][nj] == 0 and wall_visited[ni][nj] == 0:
                    visited[ni][nj] = 2
                    q.append((ni, nj))
    for k1 in range(N):
        for k2 in range(M):
            if visited[k1][k2] == 0 and wall_visited[k1][k2] == 0 and maps[k1][k2] == 0 :
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
wall_visited = [[0] * M for _ in range(N)]
max_cnt = 0
q = deque()
startpoint = []
findStart()
makeWall(0)
print(maps)
print(max_cnt)