import sys
sys.stdin = open('input.txt')
from collections import deque

# yang에서 시작할경우 BFS
def yang_BFS(yang_point):
    q.append(yang_point)
    global visited
    global result_sheep, result_wolf
    sheep, wolf = 1, 0
    while q:
        row, col = q.popleft()
        visited[row][col] = 1
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < R and 0 <= nj < C:
                if madang[ni][nj] != '#' and visited[ni][nj] == 0: # 벽이 아니고, 방문한적 없을 때
                    if madang[ni][nj] == 'o':
                        sheep += 1
                    elif madang[ni][nj] == 'v':
                        wolf += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    if sheep > wolf:
        result_sheep += sheep
    else:
        result_wolf += wolf

# 늑대에서 시작할경우 BFS
def wolf_BFS(yang_point):
    q.append(yang_point)
    global visited
    global result_sheep, result_wolf
    sheep, wolf = 0, 1
    while q:
        row, col = q.popleft()
        visited[row][col] = 1
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < R and 0 <= nj < C:
                if madang[ni][nj] != '#' and visited[ni][nj] == 0: # 벽이 아니고, 방문한적 없을 때
                    if madang[ni][nj] == 'o':
                        sheep += 1
                    elif madang[ni][nj] == 'v':
                        wolf += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    if sheep > wolf: # 양이 많을 때
        result_sheep += sheep
    else:
        result_wolf += wolf

# 기본 입력 및 선언
R, C = map(int, input().split())
madang = list(input() for _ in range(R))
visited = [[0 for _ in range(C)] for _ in range(R)]
result_sheep, result_wolf = 0, 0 # 최종 result
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()

for i in range(R):
    for j in range(C):
        if madang[i][j] == 'o' and visited[i][j] == 0 : # 양이고 방문 X실행
            yang_BFS((i, j))
        elif madang[i][j] == 'v' and visited[i][j] == 0: # 늑대고 방문 X실행
            wolf_BFS((i, j))

print(result_sheep, result_wolf)



