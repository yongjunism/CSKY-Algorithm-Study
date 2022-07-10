from collections import deque
import sys 
input = sys.stdin.readline

def bfs(start, bro):
        q = deque([(start, 0)])
        visited = [0] * 100001
        visited[start] = 1
        while q:
            sis, sec = q.popleft()
            if sis == bro:
                return sec
            if sis * 2 <= 100000 and not visited[sis*2]:
                visited[sis*2] = 1
                q.append((sis*2, sec))
            if sis + 1 <= 100000 and not visited[sis+1]:
                visited[sis+1] = 1
                q.append((sis+1, sec+1))
            if sis - 1 <= 100000 and not visited[sis-1]:
                visited[sis-1] = 1
                q.append((sis-1, sec+1))

n, k = map(int, input().split())
print(bfs(n,k))
            
        


