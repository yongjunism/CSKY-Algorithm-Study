import sys, heapq

N = int(sys.stdin.readline())
case = []
for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num :
        heapq.heappush(case,num)
    else :
        if case:
            print(heapq.heappop(case))
        else: print(0)