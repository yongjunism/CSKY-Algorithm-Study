import sys
import heapq
sys.stdin = open('input1.txt')
# s부터 후보까지 최단거리로 갈 것이다. 그런데 v1, v2를 거쳐서 !

def dijkstra(start, end):
    distance = [INF] * (n + 1)
    Q = [(0, start)]
    distance[start] = 0
    while Q:
        time, node = heapq.heappop(Q)
        if distance[node] < time: # 이미 최단거리이면 갱신할 필요 x
            continue
        for v, w in graph[node]:
            temp = time + w
            if temp < distance[v]: # 이거 조건 안걸어줘서 시간초과 났었음 @@
                distance[v] = temp
                heapq.heappush(Q, (temp, v))
    return distance[end]

input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
for tc in range(1, T+1):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, input().split()) # 예술가들의 출발지, v1, v2
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d)) # 양방향 도로
        graph[b].append((a, d))

    result = []
    for _ in range(t):
        hubo = int(input())
        GtoH = dijkstra(g, h)
        _0 = dijkstra(s, hubo)
        # 경로 s -> g -> h -> 후보
        _1 = dijkstra(s, g) + GtoH + dijkstra(h, hubo)
        # 경로  s -> h -> g -> 후보
        _2 = dijkstra(s, h) + GtoH + dijkstra(g, hubo)
        if _0 == _1 or _0 == _2:
            result.append(hubo)

    result.sort()
    print(*result)