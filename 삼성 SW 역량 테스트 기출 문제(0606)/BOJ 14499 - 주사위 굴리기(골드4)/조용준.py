import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []
dice = [0] * 6
dirs = [(1,0), (0,1), (0,-1), (-1,0)]

for _ in range(n):
    board.append(list(map(int, input().split())))

def move(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

action = list(map(int, input().split()))

for dir in action:
    dx, dy = dirs[dir % 4]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
    else:
        # nx -= dx
        # ny -= dy
        continue
    move(dir)
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])