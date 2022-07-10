import sys
sys.stdin = open('input1.txt')

input = sys.stdin.readline
V, E = map(int, input().split()) # 마을의 개수V,  E개의 도로
INF = float("inf")
distance = [[INF]*(V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, V+1): # 중간
    for i in range(1, V+1): # 시작
        for j in range(1, V+1): # 끝
            if distance[i][k] + distance[k][j] < distance[i][j]: # 최단거리 갱신이 가능하면?
                distance[i][j] = distance[i][k] + distance[k][j] # 갱신

answer = INF
for i in range(1, V+1):
    answer = min(answer, distance[i][i])

print(answer if answer != INF else -1)
