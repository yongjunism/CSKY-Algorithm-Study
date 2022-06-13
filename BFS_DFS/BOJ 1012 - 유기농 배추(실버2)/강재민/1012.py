import sys
sys.setrecursionlimit(10**6) #recursion에러 방지


def dfs(cnt,x,y) : #cnt는 몇번째 지렁이가 필요한지 체크!
    global area
    dir_ = [(0,-1),(0,1),(1,0),(-1,0)]
    area[y][x] = cnt #맨 처음 좌표 1에서 cnt로 바꿔준다 (cnt는 최소 2 이상의 수)
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
        T_C.append(list(map(int,input().split()))) #여기까지 테스트케이스 입력을 리스트에 담기 위해 작성




for _ in range(T):
    M,N,K = T_C.pop(0)
    area = [[0]*M for __ in range(N)] #가로 M 세로 N 의 area 2차원 리스트
    for __ in range(K):
        x,y = T_C.pop(0)
        area[y][x] = 1

    cnt = 2 #area내의 1과 혼동되지 않기 위해 최초 카운트를 2로 설정
    for y in range(N):
        for x in range(M):
            if area[y][x] == 1:
                dfs(cnt,x,y)
                cnt +=1
    area = [element for array in area for element in array] #2차원 배열을 1차원 배열로 list comprehension
    print(max(area)-1) #최초 cnt를 2로 설정했으므로 1 빼준다!

    # for tmp in area:
    #     print(tmp)


