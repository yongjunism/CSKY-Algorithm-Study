#1. start - V1 - V2 - end
#2. start - V2 - V1 - end

#초기세팅
import sys,heapq
input_ = sys.stdin.readline

INF = 999999999
N,E = map(int,input_().split())
graph = [[] for _ in range(N+1)]

for _ in range(E) :
    a,b,c = map(int,input_().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

V1 , V2 = map(int,input_().split())


#다익스트라 구현
def dijkstra(S,E,W): #K는 시작노드 E는 목표노드 W는 시작가중치
    
    dist = [INF] * (N+1) #시작노드에서 각각 노드사이의 최소 거리
    dist[S] = 0 #자기자신의 거리는 0
    
    hq = [] #힙큐
    heapq.heappush(hq,(W,S))
    
    while hq: #힙큐 전부 체크할때까지 반복
        wei,node = heapq.heappop(hq) #weight, node
        
        
        for e,w in graph[node] : #도착지점 end와 가중치 w
            cost = w + wei
            if cost < dist[e] :
                dist[e] = cost
                heapq.heappush(hq,(cost,e))
    
    return dist[E]

#1번 루트 
if V1 == 1: Route1_V_1 = 0
else: Route1_V_1 = dijkstra(1,V1,0)
Route1_V_2 = dijkstra(V1,V2,Route1_V_1)
if N == V2: Route1_End = Route1_V_2
else : Route1_End = dijkstra(V2,N,Route1_V_2)
        


#2번 루트
Route2_V_2 = dijkstra(1,V2,0)
Route2_V_1 = dijkstra(V2,V1,Route2_V_2)
Route2_End = dijkstra(V1,N,Route2_V_1)


#결과 출력
if Route1_End != 0 and Route2_End != 0: #모두 정상적인 경로가 있을 때
    answer = min(Route1_End,Route2_End)
    if answer == INF :
        print(-1)
    else: print(answer)
    

else: #둘중에 하나라도 정상적인 경로가 없을 때
    answer = max(Route1_End,Route2_End)
    if answer == 0 or answer == INF :
        print(-1)
    else: print(answer)
    
