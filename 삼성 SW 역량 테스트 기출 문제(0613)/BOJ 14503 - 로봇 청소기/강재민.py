N,M = map(int,input().split())
r,c,d = map(int,input().split())

case = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
NEWS = [(-1,0),(0,1),(1,0),(0,-1)] #북동남서 시계방향
answer = 0
def move(r,c,d):
    while True:
        is_continue = False
        visited[r][c] = 1
        r_tmp = r
        c_tmp = c
        for i in range(3,-1,-1) : #왼쪽(반시계)으로돌아야하니까 reverse
            if visited[r+NEWS[(d+i)%4][0]][c+NEWS[(d+i)%4][1]] == 0 and case[r+NEWS[(d+i)%4][0]][c+NEWS[(d+i)%4][1]] == 0 : #기존 방향에서 반시계방향으로 90도씩 돌려줌
                r += NEWS[(d+i)%4][0] 
                c += NEWS[(d+i)%4][1] 
                d += i     
                d = d % 4 #(-1 / 4)의 나머지는 3       
                is_continue = True
                break
        if is_continue == True: continue #이동하게되면 아래 코드 작동 중지하고 건너뜀
        
        
        if r_tmp == r and c_tmp == c:
            if case[r+NEWS[(d+2)%4][0]][c+NEWS[(d+2)%4][1]] == 1:
                return
            else: 
                r += NEWS[(d+2)%4][0] 
                c += NEWS[(d+2)%4][1] 
move(r,c,d)

for i in visited:
    answer += i.count(1)
print(answer)