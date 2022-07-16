import sys
sys.stdin = open('input2.txt')

def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M): # 모든 간선에 대해서
            cur, next, time = graph[j]  # 시작노드, 다음노드, 시간
            print(distance)
            if distance[cur] != INF and distance[next] > distance[cur] + time: # 거쳐서 가는게 빠를경우
                distance[next] = distance[cur] + time
                if i == N - 1: # 자기 자신을 제외한 N-1번 확인 한 후에 N번째에도 갱신이 발생하면 음수 cycle이 존재
                    return True
    return False

# 기본 입력
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
INF = float("inf")
distance = [INF] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A-1, B-1, C))

# 음수 cycle 여부 확인
negative_cycle = bf(0)

if negative_cycle: #negative cycle이 있으면
    print(-1)
else:
    for i in range(1, N): # 첫번째 노드를 제외하고
        if distance[i] == INF: # 가는 경로가 없으면 -1출력
            print(-1)
        else:
            print(distance[i])