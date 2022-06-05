import sys
sys.stdin = open('input4.txt')

def Rolldice(q):
    global top, down
    if q == 0 :
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif q == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif q == 2:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]
    elif q == 3:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

def MoveDice(q):
    global row, col
    di, dj = [0, 0, -1, 1], [1, -1, 0, 0] # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4 (0, 1, 2, 3)
    ni, nj = row + di[q], col + dj[q]
    if 0<= ni < N and 0 <= nj < M:
        Rolldice(q)
        if maps[ni][nj] == 0:
            maps[ni][nj] = dice[6]
        else:
            dice[6] = maps[ni][nj]
            maps[ni][nj] = 0
        print(dice[1])
        row, col = ni, nj

N, M, row, col, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
Q = list(map(int, input().split()))
dice = [0]*7 # 0,1 / 1,0 / 1,1 / 1,2 / 2,1 / 3,1
# top = dice[1] down = dice[6]

for q in Q:
    MoveDice(q-1) # q - 1 해줘야 0123으로 변함

