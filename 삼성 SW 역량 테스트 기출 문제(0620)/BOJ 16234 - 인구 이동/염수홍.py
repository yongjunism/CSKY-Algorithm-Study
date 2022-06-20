import sys
sys.stdin = open('input3.txt')
import math # 소수점 버림 math.trunc(변수)
from collections import deque

def Move():
    result = 0
    while True:
        visited = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    united = BFS((i, j))
                    if len(united) > 1:
                        number = sum([naras[x][y] for x, y in united]) // len(united)
                        for x, y in united:
                            naras[x][y] = number
                    return result
        result += 1

def BFS(point):
    q.append(point)
    united = []
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0<= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if L <= abs(naras[ni][nj] - naras[row][col]) <= R: # 두나라의 인구 차이가 범위 안에 있으면,
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    united.append((ni, nj))
    return united

N, L, R = map(int, input().split())
naras = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
result = []
q = deque()


print(Move())

