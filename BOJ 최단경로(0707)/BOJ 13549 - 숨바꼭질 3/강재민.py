import heapq
N,K = map(int,input().split())
hq = []
visited = {}
heapq.heappush(hq,(0,N))

def chk_result(n,dist) :
    if n == K:
        return dist
    else: return -1

if N == K :
    print(0)

else:
    while hq:
        dist,node = heapq.heappop(hq)

        if node in visited : continue
        else : visited[node] = 1
        
        
        #X * 2
        new_N = node * 2
        if new_N <= 100000 :
            heapq.heappush(hq,(dist,new_N))
        if chk_result(new_N,dist) != -1 : 
            print(dist)
            break   
        
        
        #X-1 
        new_N = node - 1
        if new_N >= 0 :
            heapq.heappush(hq,(dist+1,new_N))
        if chk_result(new_N,dist+1) != -1 : 
            print(dist+1)
            break
        
        #X+1
        new_N = node + 1
        if new_N <= 100000 :
            heapq.heappush(hq,(dist+1,new_N))
            
        if chk_result(new_N,dist+1) != -1 : 
            print(dist+1)
            break
        
        
            
        