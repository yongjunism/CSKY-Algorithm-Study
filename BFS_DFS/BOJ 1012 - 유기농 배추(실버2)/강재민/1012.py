import sys
sys.setrecursionlimit(10**6) #recursion에러 방지


def dfs(cnt,x,y) :
    global area
    dir_ = [(0,-1),(0,1),(1,0),(-1,0)]
    area[y][x] = cnt
    for i in dir_:
        dy = y + i[0]
        dx = x + i[1]

        if 0<=dx<M and 0<=dy<N:
            if area[dy][dx] == 1:
                area[dy][dx] = cnt
                dfs(cnt,dx,dy)


T = int(input())
T_C = []
for _ in range(T):
    T_C.append(list(map(int,input().split())))
    for __ in range(T_C[-1][2]):
        T_C.append(list(map(int,input().split())))
for _ in range(T):
    M,N,K = T_C.pop(0)
    area = [[0]*M for __ in range(N)]
    for __ in range(K):
        x,y = T_C.pop(0)
        area[y][x] = 1
    cnt = 2
    for y in range(N):
        for x in range(M):
            if area[y][x] == 1:
                dfs(cnt,x,y)
                cnt +=1
    area = [element for array in area for element in array]
    print(max(area)-1)


