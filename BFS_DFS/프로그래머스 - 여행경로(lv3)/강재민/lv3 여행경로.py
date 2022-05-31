import copy #list나 set dict 같은 mutablegks 객채는 shallow copy가 되기때문에 import 했습니다.
def solution(tickets):
    answer = []
    def dfs(ticket,visited) :
        nonlocal answer
        if not ticket: #티켓 리스트를 전부 탐방하여 빈 리스트가 되었을 경우
            tmp = copy.deepcopy(visited) #여기서 깊은복사를 하지 않게되면, visited자체는 Mutable하기때문에 answer에 추가한다고 해도 그 후에 값이 변할 수 있습니다. 그래서 깊은 복사를 해줍니다.
            answer.append(tmp)
            return
        for i in ticket: #tickets [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
            if i[0] == visited[-1] : #도착한 공항과 이제 앞으로 출발할 공항이 같은 경우 즉 "ICN" == "ICN"이면
                visited.append(i[1]) # ["ICN", "JFK"] 이므로 JFK 추가
                if ticket.index(i) == len(ticket)-1: #추가한 리스트를 ticket리스트에서 제거해주려고하는데, 만일 맨 끝에 위치해있다면
                    tmp = ticket[:-1] #맨끝만 빼줍니다.
                else : 
                    tmp = ticket[0:ticket.index(i)] + ticket[ticket.index(i)+1:] #중간 어딘가에 있다면 그 인덱스만 빼주고 합쳐줍니다.
                dfs(tmp,visited) #visited에 "JFK" 가 추가된 채로 새로운 dfs 함수를 동작합니다.
                visited.pop() #하지만 우리는 ticket리스트를 도는 for문 안에 있기 때문에 새로운 반복문을 돌기전에 pop으로 추가한 "JFK"를 빼주어야 합니다.
    dfs(tickets,["ICN"])

    return sorted(answer)[0] #탐방할 수 있는 모든 경우의 수에서 오름차순으로 정렬한뒤 맨 첫번째 경우만을 출력합니다.