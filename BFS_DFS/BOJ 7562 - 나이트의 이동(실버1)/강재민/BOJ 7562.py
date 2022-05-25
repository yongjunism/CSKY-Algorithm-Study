from collections import deque
T_C = int(input())
testCase = deque()
for _ in range(T_C*3):
    testCase.append(list(map(int,input().split())))
    
for _ in range(T_C):
    chessLen = testCase.popleft()[0]
    knight_now = testCase.popleft()
    knight_end = testCase.popleft()
    is_breaked = False
    
    
    visited = [[0] * chessLen for _ in range(chessLen)]
    visited[knight_now[0]][knight_now[1]] = 1
    knight_queue = deque([knight_now])
    while knight_queue :
        if is_breaked == True: break
        tmp = knight_queue.popleft()
        moveLoute = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        for x,y in moveLoute:
            dx = tmp[0] + x
            dy = tmp[1] + y
            
            if 0<=dx<chessLen and 0<=dy < chessLen and visited[dx][dy] == 0:
                visited[dx][dy] = visited[tmp[0]][tmp[1]] + 1
                knight_queue.append([dx,dy])
                
                if [dx,dy] == knight_end :
                    print(visited[dx][dy]-1)
                    is_breaked = True
                    break
    if not is_breaked : print(0)
