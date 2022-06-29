import sys
sys.stdin = open('input1.txt')

def CW(arr, n):
    rotated = [item[:] for item in arr]
    print(rotated)
    num = int(n//2)
    for i in range(n):
        rotated[i][num] = arr[i][i] # 주대각선 -> n/2
        rotated[i][n - i -1] = arr[i][num] # n/2 -> 보조 대각선
        rotated[num][n - i - 1] = arr[i][n - i -1] # 보조대각선 -> 가로선
        rotated[i][i] = arr[n - 1][n - i -1] # 가로선 -> 주대각선

    return rotated


def CCW():
    pass

T = int(input())
n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

print(CW(arr, n))
