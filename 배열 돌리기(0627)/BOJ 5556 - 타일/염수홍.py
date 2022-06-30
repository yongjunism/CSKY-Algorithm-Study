import sys
sys.stdin = open('input1.txt')


def Color(row, col, nums, color):
    if tile[row][col]:
        return
    print(color)
    for k1 in range(nums):  # 상
        tile[row][col + k1] = color
    for k2 in range(nums):  # 하
        tile[row + nums - 1][col + k2] = color
    for k3 in range(nums):  # 좌
        tile[row + k3][col] = color
    for k4 in range(nums):  # 우
        tile[row + k4][col + nums - 1] = color
    Color(row+1, col+1, nums-1, color + 1)



N = int(input())
K = int(input())
tile = [[0 for _ in range(N)] for _ in range(N)]
row, col = 0, 0
nums = N


Color(row, col,nums, 1)

print(tile)




for i in range(K):
    a, b = map(int, input().split())