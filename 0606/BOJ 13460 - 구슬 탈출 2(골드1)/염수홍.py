import sys
sys.stdin = open('input3.txt')
from collections import deque

# BFS를 통해서 최단거리를 구한다.
def BFS(point):
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    # 방향이 0, 1, 2, 3
    q.append(point)

    while q:
        row, col = q.popleft()
        if board[row][col] == 'O': # 구슬 탈출 @
            return
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if board[ni][nj] == '.' and visited == -1: # 빈공간인 경우에만
                visited[ni][nj] = i # 방향의 값을 넣어줍니다.
                q.append((ni, nj))



# q 혹은 visited에 방향 정보를 넣음, 갱신할 때마다 cnt하면 됨

# 10번안에 불가하면 -1 반환

# 파란 구슬은 마지막 검증을 한다.
# 해당 방향으로 움직였을 때, 길을 찾을 수 있다면 True

# test


# 기본 입출력
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [([-1] * M) for _ in range(N)] # default == -1로 설정
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            visited[i][j] = -2 # 시작점의 visited는 -2로 설정
            BFS((i, j))



print(board, visited)