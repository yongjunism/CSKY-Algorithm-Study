import sys
sys.stdin = open('input2.txt')
from collections import deque

def move(row, col, d, cnt):
    ni, nj = row + di[d], col + dj[d]
    while board[ni][nj] != '#' and board[ni][nj] != 'O':
        ni += di[d]
        nj += dj[d]
        cnt += 1
    return ni, nj, cnt

# BFS를 통해서 최단거리를 구한다.
def BFS():
    while q:
        Rrow, Rcol, Brow, Bcol, totalCnt = q.popleft()
        if totalCnt >= 10:
            print(0) # 10회 넘으면 바로 print -1하고 return
            return
        for i in range(4):
            nRrow, nRcol, Rcnt = move(Rrow, Rcol, i, 0) # move Red
            nBrow, nBcol, Bcnt = move(Brow, Bcol, i, 0) # move Blue
            if board[nBrow][nBcol] == 'O': # 파란 구슬이 O인경우
                continue
            if board[nRrow][nRcol] == 'O': # 빨간 구슬이 O에 도착한경우
                print(1)
                return
            if nRrow == nRcol and nBrow == nBcol: # 탈출 상황이 아닌데 두 구슬이 겹쳐있는경우
                if Rcnt > Bcnt: # Red가 더 많이 움직였다면
                    nRrow -= di[i]
                    nRcol -= dj[i] # 한칸 뒤로( 구슬이 겹쳐있으면 안됨)
                else:
                    nBrow -= di[i]
                    nBcol -= dj[i]
            if Rvisited[Rrow][Rcol] == 0 and Bvisited[Brow][Bcol] == 0:
                Rvisited[Rrow][Rcol] = 1
                Bvisited[Brow][Bcol] = 1
                q.append((nRrow, nRcol, nBrow, nBcol, totalCnt+1))

    print(0) # 다돌았는데 탈출 못하면 0임


# q 혹은 visited에 방향 정보를 넣음, 갱신할 때마다 cnt하면 됨

# 10번안에 불가하면 -1 반환

# 파란 구슬은 마지막 검증을 한다.
# 해당 방향으로 움직였을 때, 길을 찾을 수 있다면 True

# test


# 기본 입출력
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
Rrow, Rcol, Brow, Bcol = 0, 0, 0, 0
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
Bvisited = [([0] * M) for _ in range(N)] # blue visited
Rvisited = [([0] * M) for _ in range(N)] # Red visited
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            Rrow, Rcol = i, j
        elif board[i][j] == 'B':
            Brow, Bcol = i, j

Rvisited[Rrow][Rcol], Bvisited[Brow][Bcol] = 1, 1
q.append((Rrow, Rcol, Brow, Bcol, 0))
BFS()

