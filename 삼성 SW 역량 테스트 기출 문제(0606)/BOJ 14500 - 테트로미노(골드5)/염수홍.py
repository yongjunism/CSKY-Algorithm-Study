import sys; input = sys.stdin.readline
sys.stdin = open('input3.txt')


maxResult = 0

def DFS(row, col, Dsum, cnt):
    global maxResult
    if cnt == 4:
        maxResult = max(maxResult, Dsum)
        return
    for i in range(4):
        ni, nj = row + di[i], col + dj[i]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                DFS(ni, nj, Dsum + board[ni][nj], cnt + 1)
                visited[ni][nj] = 0

def others(row, col):
    global maxResult
    for k1 in range(4):
        temp = board[row][col]
        for k2 in range(3):
            i = (k1 + k2) % 4
            ni, nj = row + di[i], col + dj[i]
            if not (0 <= ni < N and 0 <= nj < M):
                temp = 0
                break
            temp += board[ni][nj]
        maxResult = max(maxResult, temp)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, board[i][j], 1)
        others(i, j)
        visited[i][j] = 0

print(maxResult)