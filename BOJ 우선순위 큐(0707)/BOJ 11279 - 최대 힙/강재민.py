import heapq
import sys
N = int(sys.stdin.readline())
case = []
answer = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(case,(-num,num))
    else:
        if case: 
            print(heapq.heappop(case)[1])
        else: print(0)