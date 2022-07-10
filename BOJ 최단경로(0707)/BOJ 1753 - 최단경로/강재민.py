import heapq
import sys
#초기세팅
V,E = map(int,input().split())
K = int(input())
INF = 999999999
graph = [[] for _ in range(V+1)] #기본적인 가중치는 최대값으로 설정
visited = [0] * (V+1) #노드별 방문처리

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

#출발노드 설정
answer = [INF] * (V+1)
answer[K] = 0
hq = []
heapq.heappush(hq,(0,K))

#다익스트라 시작
while hq:
    d,n = heapq.heappop(hq) #distance, node
    
    if visited[n] == 1: #방문처리
        continue
    else: visited[n] = 1
    
    for v,w in graph[n] : #시작노드의 간선들
        cost = d + w
        if cost < answer[v] : #업데이트
            answer[v] = cost
            heapq.heappush(hq,(cost,v))

#결과 출력
for i in answer[1:]:
    if i != INF :
        print(i)
    else: print('INF')