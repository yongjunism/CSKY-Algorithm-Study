from collections import deque
import sys
sys.stdin = open('input1.txt')

N, M, R = map(int, input().split())  # N*M 배열을 반시계로 R번 돌림
arr = [list(map(int, input().split())) for _ in range(N)]
# move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

def rotate():
    q = deque()
    for depth in range(min(N, M) // 2):
        row = col = depth
        for i in range(4):
            while True:
                ni, nj = row + di[i], col + dj[i]
                if depth <= ni < N - depth and depth <= nj < M - depth:
                    q.append(arr[row][col])
                    row, col = ni, nj
                else:
                    break

        # 돌린다
        for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)):
            q.appendleft(q.pop())

        for i in range(4): #큐에서 돌린 값을 넣는다
            while True:
                ni, nj = row + di[i], col + dj[i]
                if depth <= ni < N - depth and depth <= nj < M - depth:
                    arr[row][col]=q.popleft()
                    row, col = ni, nj
                else:
                    break

# 큐에서 값을 빼 저장한다
rotate()

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()