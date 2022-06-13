from collections import deque
apple = [] #사과들의 좌표 리스트
dir = {} #정수 X와 문자 C로 이루어진 딕셔너리, X초가 끝난뒤에 문자 C에 의해 방향이 바뀐다.
N = int(input()) # NXN 정사각형 보드
K = int(input()) # K개의 사과의 개수

for _ in range(K): #사과의 좌표를 apple 리스트에 옮겨담음
    tmp = list(map(int,input().split()))
    apple.append(tmp)
        
L = int(input()) #뱀의 방향전환 정보를 dir딕셔너리에 옮겨담음
for _ in range(L):
    tmp = input().split()
    dir[int(tmp[0])] = tmp[1]
    
queue_row = deque([1]) #뱀의 위치를 큐에 입력 (행)
queue_column = deque([1]) #뱀의 위치를 큐에 입력 (열)
NEWS = ['E','S','W','N'] #동남서북


i = 0
chk = NEWS[i] #현재 뱀이 움직이는 방향
cnt = 0 #몇초동안 진행되는지 카운트

while True :
    if cnt in dir.keys() : #뱀의 방향에대한 정보가 담긴 딕셔너리에서 key는 X초를 의미함 
        #현재 cnt 시간이 x초 리스트 내에 포함되어 있는가 
        if dir[cnt] == 'D' : #포함되어있다면 그 문자가 D(오른쪽방향)인가?
            i += 1
            chk = NEWS[i % 4] #0~3을 넘지않기위해 나머지값으로 해준다.
        else : #L(왼쪽방향이라면)
            i -= 1
            chk = NEWS[i % 4]
            
    cnt +=1 #시간 카운트
    
    if chk == 'E': #동쪽방향으로 진행할경우
        queue_row.append(queue_row[-1]) 
        queue_column.append(queue_column[-1]+1)
    elif chk == 'W': #서쪽방향으로 진행할경우
        queue_row.append(queue_row[-1])
        queue_column.append(queue_column[-1]-1)
    elif chk == 'N': #북쪽방향으로 진행할경우
        queue_column.append(queue_column[-1])
        queue_row.append(queue_row[-1]-1)
    else :  #남쪽방향으로 진행할경우
        queue_column.append(queue_column[-1])
        queue_row.append(queue_row[-1]+1)
    #뱀의 모든 좌표
   

    #경계조건 설정
    if queue_column[-1] == 0 or queue_column[-1] == N+1 or queue_row[-1] == 0 or queue_row[-1] == N+1 : # N * N 범위 벗어나면 break
        break
    
    breaker = False #이중for문에서 break로 한번에 탈출하기 위해, breaker함수를 정의해준다.
    for j in range(len(queue_column)-1) :
        if [queue_row[-1],queue_column[-1]] == [queue_row[j],queue_column[j]] : #뱀의 머리가 몸통을 건들이면 break
            breaker = True
    if breaker == True : break
    
    
    if [queue_row[-1],queue_column[-1]] not in apple : #뱀의 머리 좌표에 사과가 없을경우
        queue_row.popleft() #꼬리 한칸 없애버리기
        queue_column.popleft()
    else : apple.remove([queue_row[-1],queue_column[-1]]) #머리좌표에 사과가 있으면 꼬리 안없애기, 대신 사과는 사라짐
    
    
    
print(cnt) #걸린 시간 출력
    
    