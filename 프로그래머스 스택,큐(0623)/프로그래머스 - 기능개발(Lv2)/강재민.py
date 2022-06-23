import math

def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    days = []
    for i in range(length):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    while days:
        cnt = 0
        start = 0
        for i in range(len(days)):
            if start ==0 and days[i] != 0:
                start = days[i]
            if days[i] > start: break
            if days[i] != 0 and days[i]<= start :
                days[i] = 0
                cnt +=1
        days = list(filter(lambda x: x != 0,days))
        answer.append(cnt)
    
    return answer