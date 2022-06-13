import sys
sys.stdin = open('input1.txt')

N, M = map(int, input().split()) # 세로 가로
row, col, direction = map(int, input().split()) # 로봇 청소기 좌표, 방향
room = [list(map(int, input().split())) for _ in range(N)]
di, dj = [-1, 0, 1, 0], \
         [0, 1, 0, -1] # 0, 1, 2, 3, / 북동남서  왼쪽으로 바뀌면 -1씩하면됨


def Findleft(num):
    if num == 0:
        return 3
    else:
        return num-1


def Clean():
    global row, col, direction
    cnt, cleancnt = 0, 0
    while True:

        if room[row][col] == 0: # 1번 청소하기
            cnt = 0
            room[row][col] = 2 # 청소 !
            cleancnt += 1 # 청소 카운트 !
        else:
            # 왼쪽 구해주기
            left = Findleft(direction)
            li, lj = row + di[left], col + dj[left]

            if room[li][lj] == 0: # 왼쪽 청소를 안했다면 !
                row, col = li, lj # 현재 위치 갱신
                direction = left
                continue
            else:
                direction = left # 청소했을경우 방향만 왼쪽으로 변경
                cnt += 1 # 2a의 영역이 실행되었을경우 cnt해줌

        if cnt == 4:
            bi, bj = row - di[direction] , col - dj[direction] # 내 뒤쪽에 있는 애들
            if room[bi][bj] == 1:
                return cleancnt
            else:
                row, col = bi, bj  # 후진하기
                cnt = 0


    return cleancnt # 전부 다 실행되었을 경우 ccnt return

result = Clean()
print(result)