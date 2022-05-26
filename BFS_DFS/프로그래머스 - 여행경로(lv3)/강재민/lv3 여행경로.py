import copy 
def solution(tickets):
    answer = []
    def dfs(ticket,visited) :
        nonlocal answer
        if not ticket:
            tmp = copy.deepcopy(visited)
            answer.append(tmp)
            return
        for i in ticket:
            if i[0] == visited[-1] : 
                visited.append(i[1])
                if ticket.index(i) == len(ticket)-1:
                    tmp = ticket[:-1]
                else : 
                    tmp = ticket[0:ticket.index(i)] + ticket[ticket.index(i)+1:]
                dfs(tmp,visited)
                visited.pop()
    dfs(tickets,["ICN"])

    return sorted(answer)[0]