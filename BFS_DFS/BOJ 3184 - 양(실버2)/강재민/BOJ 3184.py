import sys
sys.setrecursionlimit(10**6)

Row, Column = map(int,input().split())
garden = [list(input()) for _ in range(Row)]
visited = [[0] * Column for _ in range(Row)]
final_sheep = 0
final_wolf = 0                  
            
            
def dfs(x,y):
    global area
    global visited
    dir_ = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in dir_:
        dx = x + i[0]
        dy = y + i[1]
        
        if 0<=dx < Column and 0<= dy < Row :
            if visited[dy][dx] == 0 and garden[dy][dx] !='#':
                visited[dy][dx] = 1
                area.append([dx,dy])
                dfs(dx,dy)


for y in range(Row):
    for x in range(Column):
        area = []
        sheep = 0
        wolf = 0
        if garden[y][x] != '#' and visited[y][x] == 0: #방문하지 않은 좌표이고, 경계묜아 아니라면
            dfs(x,y)

            #dfs 돌린 후 area리스트에 따라 결과가 나뉨!
            if not area: area.append([x,y])# 암것도 없으면 현재 좌표라도 한개 넣어줌
            for i in area:
                if garden[i[1]][i[0]] == 'o': #양 숫자 카운트
                    sheep +=1
                elif garden[i[1]][i[0]] == 'v': #늑대 숫자 카운트
                    wolf +=1
            if sheep > wolf: 
                final_sheep += sheep
            else: 
                final_wolf += wolf


print(final_sheep, final_wolf)