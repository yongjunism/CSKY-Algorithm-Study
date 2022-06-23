from collections import deque
def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    priorities = deque(priorities)
    while True:
        n = priorities.popleft()
        if n == max_num:
            location -= 1
            answer +=1
            if location == -1:
                return answer
            max_num = max(priorities)
        if n < max_num:
            priorities.append(n)
            location -=1
            if location ==-1:
                location = len(priorities)-1