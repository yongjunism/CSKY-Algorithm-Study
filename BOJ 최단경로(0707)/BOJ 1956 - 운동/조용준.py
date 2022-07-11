import sys 
input = sys.stdin.readline

V, E = map(int, input().split())
INF = sys.maxsize
city = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    city[a-1][b-1] = c

for k in range(V):
    
    for i in range(V):
        for j in range(V):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

ans = INF
for i in range(V):
    ans = min(ans, city[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)