N,L = map(int,input().split())
case= [list(map(int,input().split())) for _ in range(N)]

road_list = case + [list(map(lambda x: x[i], case)) for i in range(N)]

def leftcheck(idx,road,L):
    global ramp
    if road[idx] - road[idx-1] == 1:
        for i in range(L):
            if road[idx] - road[idx-i-1] == 1 and ramp[idx-i-1] == 0:
                ramp[idx-i-1] = 1
                continue
            else: 
                return False
        
        return True
    else: return True  
def rightcheck(idx,road,L):
    global ramp
    if road[idx] - road[idx+1] == 1:
        for i in range(L):
            if road[idx] - road[idx+i+1] == 1 and ramp[idx+i+1] == 0:
                ramp[idx+i+1] = 1
                continue
            else: 
                return False
        return True
    else: return True 


ans_cnt = 0
for road in road_list:
    ramp = [0] * N #경사로 설치된곳 
    # 2 2 3 2 2 3 2 2 1 1 
    is_continue = False
    for i in range(1,len(road)): #리스트 내 인접한 값들의 차이가 1을 넘으면 어차피 길 안됨 
        if abs(road[i]-road[i-1]) > 1: 
            is_continue = True
            break
    if is_continue: continue #바로 탈출
    
    answer = True
    for i in range(len(road)):
        if answer == False: break    
        
        if L == N : # 하 이거 설정 안해줘서 30분 더 머리씀
            if len(set(road)) != 1:
                answer = False
            continue
        
        if i < L:
            if road[i] - road[i+1] == 1:
                answer = rightcheck(i,road,L)
            for j in range(i):
                if road[j] < road[i]: 
                    answer = False
                    break
        
        elif i > len(road)-L-1:
            if road[i] - road[i-1] == 1:
                answer = leftcheck(i,road,L)
            for j in range(i+1,len(road)):
                if road[j] < road[i]: 
                    answer = False
                    break
        
        else:
            if road[i] - road[i+1] == 1:
                answer = rightcheck(i,road,L)
            if road[i] - road[i-1] == 1:
                answer = leftcheck(i,road,L)
    if answer == True:
        ans_cnt +=1
print(ans_cnt)