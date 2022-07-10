import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

def turn45(n, degree, arr):
    turn_cnt = abs(d) // 45
    plus = True
    if d < 0:
        plus = False

    for _ in range(turn_cnt):
        if plus:
            p_diag, i_diag = [], []
            
            for i in range(n):
                p_diag.append(arr[i][i])
            for i in range(n):
                temp = arr[i][((n+1)/2)-1]
                arr[i][((n+1)/2)-1] = p_diag[i]
                p_diag[i] = temp
            for i in range(n):
                temp = arr[i][n-i-1]
                arr[i][n-i-1] = temp[i]
                i_diag[i] = temp
            for i in range(n+1):
                temp = 
