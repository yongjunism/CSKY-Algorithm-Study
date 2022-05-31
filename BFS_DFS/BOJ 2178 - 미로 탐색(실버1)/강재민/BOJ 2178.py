from collections import deque
N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)] #가로 M에 세로 N 의 2차원 미로
queue = deque([[0,0]]) #맨 처음 좌표는 [0,0]
dir_ = [(-1,0),(0,1),(0,-1),(1,0)] #동서남북
while queue: #큐가 텅텅 빌때까지
    x,y = queue.popleft()
    if [x,y] == [M-1,N-1] : #만일 맨끝 좌표에 도달하면
        print(maze[y][x]) # 최소 칸 수 출력 하고 반복문 탈출
        break
    for i in dir_:
        dx = x + i[0]
        dy = y + i[1]

        if 0<=dx < M and 0<= dy < N:
            if maze[dy][dx] != 1: continue

            queue.append([dx,dy])
            maze[dy][dx] = maze[y][x]+1 #이전 좌표보다 한칸 더 이동했으므로 +1 해서 표시해둔다.
            

