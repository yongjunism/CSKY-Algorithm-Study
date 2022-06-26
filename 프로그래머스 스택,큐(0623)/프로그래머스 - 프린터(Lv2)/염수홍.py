from collections import deque
def solution(priorities, location):
    q = deque()
    print(priorities)
    for i in range(len(priorities)):
        if i == location:
            q.append([priorities[i], 1])
        else:
            q.append([priorities[i], 0])
    cnt = 0
    while True:
        max_num = 0
        for i in range(len(q)):
            if q[i][0] > max_num:
                max_num = q[i][0]
        if q[0][0] < max_num:
            q.append(q.popleft())
        else:
            cnt += 1
            temp = q.popleft()[1]
            if temp == 1:
                return cnt