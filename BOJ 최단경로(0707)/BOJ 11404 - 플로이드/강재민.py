import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 999999999
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)
    
for idx in range(1,N+1):
    for r in range(1,N+1):
        for c in range(1,N+1):
            if graph[r][c] > graph[idx][c] + graph[r][idx] :
                graph[r][c] = graph[idx][c] + graph[r][idx]


        
graph = [graph[i][1:] for i in range(1,N+1)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF : 
            graph[i][j] = 0
            
for i in graph:
    print(*i)
    
