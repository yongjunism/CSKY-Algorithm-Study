import sys
sys.stdin = open('input1.txt')

def Compare(new_list):
    for i in range(len(new_list)-1):
        if new_list[i] != new_list[i+1]:
            return False
    return True


def Count(matrix):
    global result
    for i in range(N):
        if Compare(matrix[i]): # 전체 행 합이 같을 때
            result += 1
        else:
            if Ramp(matrix, i): # 행검사 결과가 True일 때
                result +=1


def Ramp(matrix, i):
    visited_ground = [0] * N
    global L
    cnt = 0
    for j in range(N - 1):  # 행 검사
        cnt += 1
        if matrix[i][j + 1] - matrix[i][j] == 1:  # 올리가는거
            if cnt >= L: # 내가 쌓아온 갯수랑 L의
                for l in range(L):
                    if visited_ground[j-l] == 0:
                        visited_ground[j-l] = 1
                    else: # visited 가 있는 경우가 있다면
                        return False
                cnt = 0
            else:
                return False
        elif matrix[i][j + 1] - matrix[i][j] == -1:  # 내려가는거
            cnt, temp_sum = 0, 0 # cnt 필요 없어져서 초기화
            for l in range(L):
                if j+1+l < N:
                    temp_sum += matrix[i][j+1+l]
                    visited_ground[j+1+l] = 1
                else:
                    return False
            if matrix[i][j+1] * L != temp_sum: # 내리막길 경사가 불가능하면
                return False
            else: # 가능하면
                temp_sum = 0 # 초기화
        elif abs(matrix[i][j + 1] - matrix[i][j]) > 1: # 높이차이가 2칸이상 나면 가망 없음
            return False
    return True

N, L = map(int, input().split()) # N개의 줄 L의 길이 경사로
ground = [list(map(int, input().split())) for _ in range(N)]
newground = list(zip(*ground)) # 전치행렬 만들어주기
# visited_ground = [[0]*N for _ in range(N)]
# visited_newground = [[0]*N for _ in range(N)]
result = 0

Count(ground)
Count(newground)

print(result)
