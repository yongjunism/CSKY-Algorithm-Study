N,M = map(int,input().split())
max_num = 0 #정답
case = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)] 
max_val = max(map(max,case))

def dfs(idx,r,c,sum):
    global max_num
    
    # if max_num >= sum + max_val * (3-idx) :
    #     return
    
    # if idx == 3:
    #     max_num = max(sum,max_num)
    #     return
        
    
    dir_ = [(1,0),(-1,0),(0,-1),(0,1)]
    
    for i in dir_ :
        dr = r + i[0]
        dc = c + i[1]
        
        if 0<=dr<N and 0<=dc<M:
            if idx == 1 and visited[dr][dc] == 0: #ㅗ모양 탐색
                visited[dr][dc] = 1
                dfs(2,r,c,sum+case[dr][dc])
                visited[dr][dc] = 0 #방문기록 초기화
            if visited[dr][dc] == 0:  
                visited[dr][dc] = 1
                dfs(idx+1,dr,dc,sum+case[dr][dc])
                visited[dr][dc] = 0 #방문기록 초기화


#메인 함수
for Row in range(N):
    for Column in range(M):
        visited[Row][Column] = 1
        dfs(0,Row,Column,case[Row][Column])
        visited[Row][Column] = 0 #방문기록 초기화
        
print(max_num)