# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력 1 
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1 
# 15

# from collections import deque

# N,M = list(map(int,input().split()))
# maze = [list(map(int,input()))for _ in range(N)]


# q = deque()
# q.append((0,0))
# d= [(-1,0),(1,0),(0,-1,),(0,1)]

# breaker = False
    
# while True:
#     x, y = q.popleft()
#     for i in range(len(d)) :
#         dx = x + d[i][0]
#         dy = y + d[i][1]
#         if 0<=dx < N and 0<=dy<M:
#             if maze[dx][dy] == 1 :
#                 maze[dx][dy] = maze[x][y]+1
#                 q.append((dx,dy))
#             if dx == N-1 and dy == M-1 :
#                 print(maze[dx][dy])
#                 breaker = True
#     if breaker == True : 
#         break





from collections import deque
N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
queue = deque([[0,0]])
dir_ = [(-1,0),(0,1),(0,-1),(1,0)]
while queue:
    x,y = queue.popleft()
    if [x,y] == [M-1,N-1] : 
        print(maze[y][x])
        break
    for i in dir_:
        dx = x + i[0]
        dy = y + i[1]

        if 0<=dx < M and 0<= dy < N:
            if maze[dy][dx] != 1: continue

            queue.append([dx,dy])
            maze[dy][dx] = maze[y][x]+1
            

