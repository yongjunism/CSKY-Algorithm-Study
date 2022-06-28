from collections import deque
c,r = map(int,input().split())
R = r 
C = c
K = int(input())
area = [[0] * c for _ in range(r)]
r -=1
c = 0
area[r][c] = 1
dir_ = deque([(-1,0),(0,1),(1,0),(0,-1)])
cnt = 1
answer = []
if K > R*C: 
    print(0)
elif K == 1:
    print('1 1')
else:   
    while cnt < R*C :
        cnt +=1
        while True :
            dr = r + dir_[0][0]
            dc = c + dir_[0][1]
            if 0<=dr< R and 0<=dc < C and area[dr][dc] == 0:
                area[dr][dc] = cnt
                r = dr
                c = dc
                break
            else: dir_.rotate(-1)
        
        if cnt == K:
            answer = [c+1,R-r]
            break
    if answer :
        print(*answer)
    else: print(0)

