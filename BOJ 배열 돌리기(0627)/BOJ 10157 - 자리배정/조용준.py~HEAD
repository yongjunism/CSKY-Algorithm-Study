import sys
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

visited = [[0] * c for _ in range(r)]

num, dir = 1, 0
x, y = r-1, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if k > r*c:
        print(0)
        break
    if num == k:
        print(y+1, r-x)
        break
    visited[x][y] = num
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= r or ny >= c or visited[nx][ny]:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    num += 1