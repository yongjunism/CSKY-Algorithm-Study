from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append((nx, ny))

tc = int(input())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(tc):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
    
    for x in range(n):
        for y in range(m):
            if field[x][y] == 1:
                bfs(x, y)
                field[x][y] = 0
                cnt += 1
    print(cnt)