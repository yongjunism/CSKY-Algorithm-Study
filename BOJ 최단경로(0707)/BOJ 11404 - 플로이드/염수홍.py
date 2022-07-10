import sys
sys.stdin = open('input1.txt')

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = float("inf")
distance = [[INF]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if distance[a-1][b-1] > c:
        distance[a-1][b-1] = c

for k in range(n): # 경유
    for i in range(n):  # 시작
        for j in range(n): # 도착
            if i != j and distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
