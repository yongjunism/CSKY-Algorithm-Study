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
        if garden[y][x] != '#' and visited[y][x] == 0: 
            dfs(x,y)
            if not area: area.append([x,y])
            for i in area:
                if garden[i[1]][i[0]] == 'o':
                    sheep +=1
                elif garden[i[1]][i[0]] == 'v':
                    wolf +=1
            if sheep > wolf: 
                final_sheep += sheep
            else: 
                final_wolf += wolf


print(final_sheep, final_wolf)