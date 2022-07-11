import sys, heapq

N = int(sys.stdin.readline())
case = []
answer =[]
for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num :
        heapq.heappush(case,(abs(num),num))
    else :
        if case:
            print(heapq.heappop(case)[1])
        else: print(0)
