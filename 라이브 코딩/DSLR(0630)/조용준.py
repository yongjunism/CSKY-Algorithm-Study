from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque([(start, '')])
    visited = [0] * 10000
    visited[start] = 1

    while q:
        num, op = q.popleft()
        if num == end: 
            return op
        if num*2 <= 9999 and not visited[num*2]:
            visited[num*2] = 1
            q.append((num*2, op+'D'))
        if num*2 > 9999 and not visited[num*2 % 10000]:
            visited[num*2 % 10000] = 1
            q.append((num*2 % 10000, op+'D'))
        if num != 0 and not visited[num-1]:
            visited[num-1] = 1
            q.append((num-1, op+'S'))
        if num == 0 and not visited[9999]:
            visited[9999] = 1
            q.append((9999, op+'S'))
        if not visited[num%1000 * 10 + num//1000]:
            visited[num%1000 * 10 + num//1000] = 1
            q.append((num%1000 * 10 + num//1000, op+'L'))
        if not visited[num%10 * 1000 + num//10]:
            visited[num%10 * 1000 + num//10] = 1
            q.append((num%10 * 1000 + num//10, op+'R'))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a,b))

# 1234 -> 2341
# 1234 // 1000 = 1
# 1234 % 1000 = 234 * 10 = 2340

# 4123 -> 3412
# 4123 % 10 = 3 * 1000 = 3000
# 4123 // 10 = 412 
# 3000 + 412 = 3412