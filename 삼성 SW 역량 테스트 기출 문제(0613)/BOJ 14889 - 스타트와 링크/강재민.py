N = int(input())

case = [list(map(int,input().split())) for _ in range(N)]
answer = 100
start_team = []
def backtracking(idx):
    global answer
    if len(start_team)>=N/2 : #스타트팀 리스트에 전체 인구의 절반이 채워졌다면
        start_power = 0
        link_power = 0
        link_team = []
        for i in range(N): #링크팀에 나머지 사람들 넣어줍니다.
            if i not in start_team:
                link_team.append(i)
        for x in start_team: #스타트 팀의 능력치의 합
            for y in start_team:
                start_power += case[x][y]
        for x in link_team: #링크 팀의 능력치의 합
            for y in link_team:
                link_power += case[x][y]
        answer = min(answer,abs(start_power-link_power)) #기존 정답과 신 정답 간 최소치 비교 후 갱신
        return
    
    for i in range(idx+1,N):#백트래킹
        start_team.append(i)
        backtracking(i)
        start_team.pop()
backtracking(-1) #이렇게 해야 0부터 시작함
print(answer)