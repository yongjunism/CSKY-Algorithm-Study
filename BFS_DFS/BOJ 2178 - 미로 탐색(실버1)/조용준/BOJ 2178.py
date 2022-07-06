from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1
dir = [(-1, 0), (1, 0), (0, -1), (0,1)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist[n-1][m-1]

print(bfs(0, 0))
