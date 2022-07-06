N = int(input())
K = int(input())
tile = [list(map(int,input().split())) for _ in range(K)]

for i in tile:
    print(i)

for c,r in tile: #절반이상의 좌표를 넘어가면 대칭을 해준다.
    
    if c > int(N/2):
        c = N-c+1
    if r > int(N/2):
        r = N-r+1
    
    ans = (min(r,c)-1) % 3
    print(ans+1)
    
    