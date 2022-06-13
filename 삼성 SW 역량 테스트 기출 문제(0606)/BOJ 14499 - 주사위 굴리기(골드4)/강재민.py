from collections import deque

N,M,x,y,K = map(int,input().split())

Column = deque([4,1,3])
Row = deque([2,1,5,6])
dice_Value = {1:0,2:0,3:0,4:0,5:0,6:0}

area = [list(map(int,input().split())) for _ in range(N)]
movement = list(map(int,input().split()))

for i in movement:
    if i == 1: #동쪽으로 이동하는 경우
        y +=1
        if y>=M : #경계 벗어나면 원 상태 복구 후 탈출
            y-=1
            continue
        
        Column.rotate(1) #열 한칸 이동
        Row[1] = Column[1] #Row와 Column이 겹치는 칸은 맨위밖에 없기때문에, Column이 바꼈으므로 Row[1]도 동시 업데이트 해줘야함
        
        tmp = Column[0] #엑셀 참고 
        Column[0] = Row[3]
        Row[3] = tmp
        

    
    elif i == 2: #서쪽으로 이동하는 경우
        y -= 1
        if y <0 : #경계 벗어나면 원 상태 복구 후 탈출
            y +=1
            continue
        
        Column.rotate(-1)
        Row[1] = Column[1]
        tmp = Column[2]
        Column[2] = Row[3]
        Row[3] = tmp

    
    elif i==3: #북쪽으로 이동하는 경우
        x -= 1
        if x < 0:
            x+=1
            continue
        Row.rotate(-1)
        Column[1] = Row[1]
    
    else: #남쪽으로 이동하는 경우
        x +=1
        if x>=N:
            x -=1
            continue
        Row.rotate(1)
        Column[1] = Row[1]
        
        
    #주사위와 지도 간 숫자 교환
    if area[x][y] == 0: #지도에 숫자가 0이라면
        area[x][y] = dice_Value[Row[3]] #주사위 맨밑 숫자 복사해줌
    else:
        dice_Value[Row[3]] = area[x][y] #0이 아니라면 주사위에 복사해줌
        area[x][y] = 0 #지도 숫자는 사라짐

    print(dice_Value[Row[1]])
