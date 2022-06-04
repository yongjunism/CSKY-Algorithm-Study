import sys
sys.stdin = open('input1.txt')
from collections import deque

def Rotate(head, direction):
    if direction[1] =='D':
        if head == 3:
            return 0
        else:
            return head + 1
    # 시계방향이니까 1씩 늘리면 오른쪽으로 회전함 , 3일경우 1반환
    elif direction[1] == 'L':
        if head == 0:
            return 3
        else:
            return head - 1
    # 반시계방향 -1씩 줄이면 왼쪽으로 90도 회전 , 1일경우 4반환

def Move(row, col, ni, nj):
    if 0 <= ni < N and 0<= nj < N: # 범위 안에 있으면
        q.appendleft((row, col))
        q.appendleft((ni, nj))

        if board[ni][nj] == 2:  # 사과를 만났을 경우
            board[ni][nj] = 1
            return True
        elif board[ni][nj] == 1: # 꼬리 만난 경우
            return False
        else:
            board[ni][nj] = 1  # 사과가 없을 경우
            if len(q) >= 2:
                erow, ecol = q.pop() # 꼬리를 한칸 지워준다
                board[erow][ecol] = 0
                return True
            else:
                return False

    else: # 없으면 게임 끝
        return False


def Game():
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]  # 오른쪽 아래 왼쪽 위 시계방향
    q.append((0, 0))
    sec, head = 0, 0  # 뱀의 대가리 위치 초기값 0,0, 오른쪽, 시간 초기화
    while q:
        row, col = q.popleft() # 대가리의 정보
        board[row][col] = 1
        # Move
        ni, nj = row + di[head], col + dj[head]
        move_result = Move(row, col, ni, nj)
        sec += 1 # move 1회마다 sec 1증가
        if move_result == False: # 벽을 만났다면
            return sec #게임 끝
        else:
            for direction in directions:
                if sec == int(direction[0]):  # 이벤트가 발생하는 초인 경우에 Change direction
                    head = Rotate(head, direction)

# 기본 입력 및 사과의 위치 표시
N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2 # 사과의 위치 표시
L = int(input()) # 방향 변환 횟수
directions = deque()
directions = [list(input().split()) for _ in range(L)] # X초가 끝날 떄,
# D방향으로 변환 (D일경우 오른쪽 90도 변환, C일경우 왼쪽 90도 변환)
q = deque()
print(Game())



