from collections import deque
N,M = map(int, input().split())

maze = [list(map(int,input().split()))for _ in range(N)]
dir_ = [(-1,0),(0,1),(1,0),(0,-1)]
maze_virus = []
for y in range(N):
        for x in range(M) :
            if maze[y][x] == 2: maze_virus.append((x,y))
answer = 0

def bfs(maze) :
    global answer
    q = deque(maze_virus)
    visited = [[0]*M for _ in range(N)]
    save_area = 0
    
    while q:
        x,y = q.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            for i in dir_:
                dy = y + i[0]
                dx = x + i[1]

                if 0<=dx < M and 0<=dy < N:
                    if maze[dy][dx] == 0:
                        maze[dy][dx] = 2
                        q.append((dx,dy))
                        
    for i in maze:
        save_area += i.count(0)
    answer = max(answer,save_area) #정답 갱신
    

num_list = []
def backtracking(idx): #맵에서 value가 0인것 3개를 찾는 백트래킹
    if len(num_list) == 3 : 
        one = (num_list[0] // M ,num_list[0] % M)
        two = (num_list[1] // M ,num_list[1] % M)
        three = (num_list[2] // M ,num_list[2] % M)
        tmp_maze = list(map(lambda x : x[:],maze))
        
        #3개를 다 찾았다면 벽을 세워준다.
        tmp_maze[one[0]][one[1]] = 1
        tmp_maze[two[0]][two[1]] = 1
        tmp_maze[three[0]][three[1]] = 1
        bfs(tmp_maze) #새롭게 새워진 벽으로 bfs탐색 시작
        return
    for i in range(idx+1,N*M):#백트래킹
        if maze[i // M][i % M] == 0:
            num_list.append(i)
            backtracking(i)
            num_list.pop()
            
backtracking(-1) #이렇게 해야 0부터 시작함
print(answer)