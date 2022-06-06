#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

# 예제 입력 1 
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
# 예제 출력 1 
# 9
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
ESWN = ['E','S','W','N'] #동남서북


i = 0
chk = ESWN[i] #현재 뱀이 움직이는 방향
cnt = 0 #몇초동안 진행되는지 카운트

while True :
    if cnt in dir.keys() : #뱀의 방향에대한 정보가 담긴 딕션어리에서 key는 X초를 의미함 
        #현재 cnt 시간이 x초 리스트 내에 포함되어 있는가 
        if dir[cnt] == 'D' : #포함되어있다면 그 문자가 D(오른쪽방향)인가?
            i += 1
            chk = ESWN[i % 4] #0~3을 넘지않기위해 나머지값으로 해준다.
        else : #L(왼쪽방향이라면)
            i -= 1
            chk = ESWN[i % 4]
            
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
    
   

    #경계조건 설정
    if queue_column[-1] == 0 or queue_column[-1] == N+1 or queue_row[-1] == 0 or queue_row[-1] == N+1 : #N X N 범위 벗어나면 break
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
    
    