import sys
import heapq


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
N, M = map(int, input().split()) # 헛간과 길
INF = float("inf")
graph = [[] for _ in range(N + 1)]

# draw graph
for _ in range(M):
    a, b, c = map(int, input().split()) # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))


print(dijkstra(1, N))

