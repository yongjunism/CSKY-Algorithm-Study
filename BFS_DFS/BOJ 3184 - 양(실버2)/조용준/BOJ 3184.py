from collections import deque
import sys
input = sys.stdin.readline

def dfs(x, y):
    global o
    global v
    visited[x][y] = 1
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < row and 0 <= ny < col:
            if yard[nx][ny] != '#' and visited[nx][ny] == 0:
                if yard[nx][ny] == 'o':
                    o += 1
                if yard[nx][ny] == 'v':
                    v += 1
                dfs(nx, ny)

row, col = map(int, input().split())

yard = [list(input().rstrip()) for _ in range(row)]
dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [[0] * col for _ in range(row)]
sheep, wolf, o, v = 0, 0, 0, 0

for i in range(row):
    for j in range(col):
        if yard[i][j] != '#' and visited[i][j] == 0:
            if yard[i][j]=='o':
                o += 1
            if yard[i][j]=='v':
                v += 1
            dfs(i, j)
            if v < o:
                sheep += o
            else:
                wolf += v
            o, v = 0, 0

print(sheep, wolf)