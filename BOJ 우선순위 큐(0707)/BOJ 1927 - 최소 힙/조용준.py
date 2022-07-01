import sys, heapq
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)