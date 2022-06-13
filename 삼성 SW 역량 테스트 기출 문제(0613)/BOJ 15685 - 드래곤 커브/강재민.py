N = int(input())

curv = [list(map(int,input().split())) for _ in range(N)]
area = [[0] * 101 for _ in range(101)] #area[y][x]
dir_ = [(1,0),(0,-1),(-1,0),(0,1)]
def dragon_curv(x,y,d,g,dragon_body):
    global area
    if g<0 : 
        for i in set(dragon_body):
            area[i[1]][i[0]] = 1
        return
    if len(dragon_body) == 1:
        dy = y + dir_[d][1]
        dx = x + dir_[d][0]
        dragon_body.append((dx,dy))
        dragon_curv(x,y,d,g-1,dragon_body)
        return
    #기준점 (a,b)이고 x,y를 기준점으로부터 90도 회전하는법 :
    # x간격 : a-x
    # y간격 : b-y
    # 이동 후 좌표 : ((a+y간격),(b-x간격))
    a,b = dragon_body[-1]
    for i in reversed(dragon_body): #맨 마지막 좌표의 회전이 
        #그다음 기준점이 되려면 reversed를 해주어야함
        new_x = a + (b-i[1])
        new_y = b - (a-i[0])
        if 0<=new_x<101 and 0<=new_y<101:
            if (new_x,new_y) not in dragon_body:
                dragon_body.append((new_x,new_y))
    dragon_curv(x,y,d,g-1,dragon_body)
    
    
#메인함수
for i in curv:
    dragon_curv(i[0],i[1],i[2],i[3],[(i[0],i[1])])

#영역내에서 1x1직사각형을 이룬 개수 찾기
answer = 0
for i in range(100):
    for j in range(100):
        if area[i][j] == 1 and area[i+1][j] == 1 and area[i][j+1] == 1 and area[i+1][j+1] == 1:
            answer +=1
#결과 출력
print(answer)