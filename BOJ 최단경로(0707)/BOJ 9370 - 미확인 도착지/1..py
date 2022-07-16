import sys, heapq
sys.stdin = open('input1.txt')
input = sys.stdin.readline
T_C = int(input())
INF = int(1e9)

# 테케 시작
for _ in range(T_C):

    n, m, t = map(int, input().split())  # 첫번째 줄 : 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split())  # 두번째 줄 : 출발지, 경유지1, 경유지2
    graph = [[] for _ in range(n + 1)]
    des_list = []  # destination list
    for _ in range(m):
        a, b, d = map(int, input().split())  # a와 b사이에 길이 d의 양방향 도로
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):  # 목적지 후보군들
        des_list.append(int(input()))

    def dijkstra(start, cost):
        dist = [INF] * (n + 1)
        dist[start] = cost
        hq = []
        visited = {}
        heapq.heappush(hq, (cost, start))
        while hq:
            wei, node = heapq.heappop(hq)
            if node in visited:
                continue
            else:
                visited[node] = 1
            for dest, cost in graph[node]:
                new_cost = cost + wei
                if new_cost < dist[dest]:
                    dist[dest] = new_cost
                    heapq.heappush(hq, (new_cost, dest))
        return dist

    # 루트1 : s -> g -> h  -> destination
    # 루트 2: s -> h -> g -> destination
    # 루트 3 : s -> destination

    G_H_WEIGHT = dijkstra(g, 0)[h]
    # 루트 1 (g에서의 가중치 + g-h사이의 가중치)를 가지고 h에서 시작하면됨
    if s == g:
        g_1 = 0
    else:
        g_1 = dijkstra(s, 0)[g]
    h_1 = g_1 + G_H_WEIGHT
    des_1 = dijkstra(h, h_1)
    print(des_1)

    # 루트 2 (h에서의 가중치 + g-h사이의 가중치)를 가지고 g에서 시작하면됨
    if s == g:
        h_2 = 0
    else:
        h_2 = dijkstra(s, 0)[h]
    g_2 = h_2 + G_H_WEIGHT
    des_2 = dijkstra(g, g_2)
    print(des_2)

    # 루트 3
    des_3 = dijkstra(s, 0)
    print(des_3)

    # 결과값 출력
    answer = []
    for i in des_list:
        if des_3[i] == des_1[i] or des_3[i] == des_2[i]:
            answer.append(i)

    print(*sorted(answer))