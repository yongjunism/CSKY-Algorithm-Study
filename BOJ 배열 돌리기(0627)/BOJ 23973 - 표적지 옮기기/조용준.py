import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip().split()) for _ in range(n)]
candidates = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            candidates.append((i,j))

MAX = 1
for i in range(len(candidates)):
    for j in range(i+1, len(candidates)):
        dist = 