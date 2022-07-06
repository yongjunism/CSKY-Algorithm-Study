import heapq
from collections import deque


def Add(q, sec, working):
    while q:
        if q[0][0] > sec:
            return
        heapq.heappush(working, [q[0][1], q[0][0]])
        q.popleft()



def solution(jobs):
    N = len(jobs)
    jobs.sort(key=lambda x: x[1])
    q = deque(jobs)
    sec = 0
    time = 0# 현재시간
    working = []
    i = 0
    while i < len(jobs):
        Add(q, sec, working)
        if len(working) > 0:
            current = heapq.heappop(working)
            sec += current[0] # 현재시간
            start = current[1]
            time += (sec - start)
            i += 1
        else:
            sec += 1
    print(time // N)


solution([[0, 3], [1, 9], [2, 6]])