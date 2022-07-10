import sys
import heapq
sys.stdin = open('input1.txt')

def dijkstra(start, end):
    visited = [0] * (N + 1)
    distance = [INF] * (N + 1)
    Q = [(0, start)]
    while Q:
        time, node = heapq.heappop(Q)
        if visited[node] == 0:
            distance[node] = time
            visited[node] = 1
            for v, w in graph[node]:
                temp = time + w
                heapq.heappush(Q, (temp, v))
    return distance[end]

input = sys.stdin.readline
N, E = map(int, input().split()) # 정점의 개수, 간선의 개수
INF = float("inf")
graph = [[] for _ in range(N + 1)]


# draw graph
for _ in range(E):
    a, b, c = map(int, input().split()) # 양방향 길과 거리
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) # 반드시 지나야하는 정점

# 경로 ver1) 1 -> v1 -> v2 -> N
_1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# 경로 ver2) 1 -> v2 -> v1 -> N
_2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if min(_1, _2) != INF:
    print(min(_1, _2))
else:
    print(-1)

