from collections import deque
N,M = map(int, input().split())
#----------------------초기 세팅------------------------------
maze = [list(map(int,input().split()))for _ in range(N)] #연구소
dir_ = [(-1,0),(0,1),(1,0),(0,-1)] #상하좌우

maze_virus = [] #바이러스 리스트
for y in range(N):
        for x in range(M) :
            if maze[y][x] == 2: maze_virus.append((x,y)) #바이러스 리스트 완성합니다
answer = 0 #안전 영역의 최대크기

#앞으로 할일 :
#1.맵에서 안전영역중에 3개를 백트래킹으로 찾아서 벽을 세웁니다.
#2. 그 벽을 세운 임시 연구소에서 bfs로 바이러스를 퍼트립니다.
#3. 살아남은 안전구역이 기존 안전구역 최대값보다 클 경우 새로 갱신해 줍니다.  

#----------------------bfs함수------------------------------
def bfs(maze) : #연구소 내에서 바이러스가 퍼지는 bfs함수
    #이때 maze는 아까 복사해둔 복제품이기 때문에 실제 maze에 영향 x
    global answer
    q = deque(maze_virus)
    visited = [[0]*M for _ in range(N)]
    save_area = 0
    
    while q: #바이러스 몽땅 퍼지기 시작합니다!!!!
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
                        
    for i in maze: #살아남은 area 평수 체크
        save_area += i.count(0)
    answer = max(answer,save_area) #안전 영역의 크기가 지금까지 안전영역의 
    #최대 크기보다 크다면 정답 갱신
    
#----------------------백트래킹 함수------------------------------
num_list = []
def backtracking(idx): #맵에서 value가 0인것 3개를 찾는 백트래킹
    if len(num_list) == 3 : 
        one = (num_list[0] // M ,num_list[0] % M)
        two = (num_list[1] // M ,num_list[1] % M)
        three = (num_list[2] // M ,num_list[2] % M)
        tmp_maze = list(map(lambda x : x[:],maze)) #연구소 deepcopy한 연구소 테스트용 2차원 복제품
        
        #3개를 다 찾았다면 벽을 세워준다.
        tmp_maze[one[0]][one[1]] = 1
        tmp_maze[two[0]][two[1]] = 1
        tmp_maze[three[0]][three[1]] = 1
        bfs(tmp_maze) #새롭게 새워진 벽으로 bfs탐색 시작
        return
    for i in range(idx+1,N*M):# 벽을 세우기 위한 백트래킹
        if maze[i // M][i % M] == 0:
            num_list.append(i)
            backtracking(i)
            num_list.pop()
            
#----------------------메인 함수------------------------------
backtracking(-1) #이렇게 해야 0부터 시작함
print(answer)