import sys
sys.stdin = open('input1.txt')
from collections import deque
def BFS():
    q = deque()
    q.append(N)
    visited = [0 for _ in range(100001)]
    visited[N] = 1
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]
        if 0<= cur-1 < 100001 and visited[cur-1] == 0:
            visited[cur-1] = visited[cur] + 1
            q.append(cur-1)
        if 0<= cur * 2 < 100001 and visited[cur * 2] == 0:
            visited[cur * 2] = visited[cur] # 0초니까 안 더해줌
            q.append(cur*2)
        if 0<= cur + 1 < 100001 and visited[cur + 1] == 0:
            visited[cur + 1] = visited[cur] + 1
            q.append(cur + 1)

N, K = map(int, input().split())
print(BFS()-1)
