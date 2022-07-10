import sys
sys.stdin = open('input1.txt')

def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M): # 모든 간선에 대해서
            cur = graph[j][0] # 시작노드, 현재노드
            next = graph[j][1] # 도착노드, 다음노드
            time = graph[j][2] # 시간 소요시간
            if distance[cur] != INF and distance[next] > distance[cur] + time: # 거쳐서 가는게 빠를경우
                distance[next] = distance[cur] + time
                if i == N - 1:
                    return True
    return False

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
INF = float("inf")
distance = [INF] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A-1, B-1, C))

negative_cycle = bf(0)

if negative_cycle: #negative cycle이 있으면
    print(-1)
else:
    for i in range(1, N): # 첫번째 노드를 재외하고
        if distance[i] == INF: # 가는 경로가 없으면 -1출력
            print(-1)
        else:
            print(distance[i])