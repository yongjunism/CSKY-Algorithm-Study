import sys 
input = sys.stdin.readline

n = int(input())
k = int(input())
removed = [list(map(int, input().split())) for _ in range(k)]

art = [[0]*n for _ in range(n)]

# 주대각선
for i in range(n):
    if i % 3 == 1:
        art[i][i] = 2
    elif i % 3 == 2:
        art[i][i] = 3
    else:
        art[i][i] = 1
    
art[i][i] = 
