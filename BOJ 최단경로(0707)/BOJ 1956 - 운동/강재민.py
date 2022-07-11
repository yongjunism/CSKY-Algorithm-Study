import sys

input = sys.stdin.readline

INF = 999999999
V,E = map(int,input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E) :
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for idx in range(1,V+1):
    for r in range(1,V+1):
        for c in range(1,V+1):
            cost = graph[idx][c] + graph[r][idx]
            if graph[r][c] > cost:
                graph[r][c] = cost
                
answer = INF

for i in range(V+1):
    answer = min(answer,graph[i][i])
    
if answer == INF : print(-1) 
else : print(answer)
    