def distribute(progresses):
    answer = []
    cnt = 0
    while progresses:
        if progresses[0] != 100:
            if cnt > 0:
                return cnt
            else:
                return cnt
        else:  # 100이 맞으면
            progresses.pop(0)
            cnt += 1
    return cnt

def solution(progresses, speeds):
    result = []
    while len(progresses) > 0:
        for idx in range(len(progresses)):
            if progresses[idx] + speeds[idx] <= 100:
                progresses[idx] += speeds[idx]
            else:
                progresses[idx] = 100
        if progresses[0] == 100:
            answer = distribute(progresses)
            if answer > 0:
                result.append(answer)
    return result