import sys
sys.stdin = open('input1.txt')
import heapq

def dijkstra():
    while Q:
        time, node = heapq.heappop(Q)
        if visited[node] == 0: # 방문한 적이 없다면
            distance[node] = time # 시간을 갱신해줌
            visited[node] = 1
            for v, w in graph[node]: # 현재 노드에서 갈 수 있는 애들 탐색 (v: 다음 노드, w : 가중치,거리,시간)
                temp = time + w # 새로운 가중치 갱신
                heapq.heappush(Q, (temp, v))

input = sys.stdin.readline
INF = float("inf")
V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E

graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1) # 방문 체크
distance = [INF] * (V + 1) # 거리

K = int(input()) # 시작 정점의 번호

for _ in range(E):
    u, v, w = map(int, input().split()) # u에서 v로가는 가중치 w인 간선
    graph[u].append((v, w))

Q = [(0, K)]

dijkstra() # 다익스트라 실행

# 출력
for i in range(1, V+1):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])

# print(graph)
# print(visited)
# print(distance)