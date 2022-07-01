import sys
sys.stdin = open('input.txt')
from collections import deque

def D(point):
    if int(point//2) < 0:
        return str(point % 2)
    else:
        return str(int(point/2))

def S(point):
    if point == 9999:
        return '0'
    else:
        return str(point + 1)

def L(point):
    if len(point) < 4:
        point = '0' * (4-len(point))  + point
    return point[-1] + point[0:3]

def R(point):
    if len(point) < 4:
        point = '0' * (4-len(point))  + point
    return point[1:4] + point[0]

def BFS(end):
    global visited
    q = deque()
    q.append(end)
    cnt = 0
    while q:
        point = q.popleft()
        dx = [D(int(point)), S(int(point)), L(point), R(point)]
        ABC = ['d', 's', 'l', 'r']
        for d in dx:
            if int(point) == int(start) or int(d)==int(start) : # start에 도달하면
                return
        cnt += 1
        for i in range(4):
            next_point = dx[i]
            if 0 <= int(next_point) < 10000 and int(next_point) not in visited:
                print(ABC[i], cnt)
                q.append(next_point)
                visited[int(next_point)].append(next_point)
                parent[int(next_point)] = [point, ABC[i]]



T = int(input())
for tc in range(1, T+1):
    start, end = input().split()
    visited = [[] for _ in range(10000)]
    parent = [[] for _ in range(10000)]
    d, s, l, r = 0, 0, 0, 0

    BFS(end)
    print(visited)
    print(parent)