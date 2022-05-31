import sys
sys.stdin = open('input.txt')
from collections import deque


def BFS():
    visited = [[0 for _ in range(I)] for _ in range(I)]
    visited[start_row][start_col] = 1
    while q:
        row, col = q.popleft()
        if visited[end_row][end_col] != 0 :
            return visited[end_row][end_col] -1
        for i in range(8):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < I and 0 <= nj < I:
                if visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1


# 기본 입력 및 선언
T = int(input())
for tc in range(T):
    I = int(input())
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())
    di = [1, 1, 2, 2, -1, -1, -2, -2]
    dj = [2, -2, 1, -1, 2, -2, 1, -1]
    q = deque()
    q.append((start_row, start_col))

    # BFS 실행
    result = BFS()
    print(result)


