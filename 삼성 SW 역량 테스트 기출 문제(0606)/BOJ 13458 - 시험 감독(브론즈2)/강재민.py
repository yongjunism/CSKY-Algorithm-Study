N = int(input())
case = list(map(int,input().split()))
answer = 0
head, assistent = map(int,input().split())

for i in case:
    if i-head <0: # 딱 맞게 떨어지면
        answer +=1 #종료
        continue
    if ((i-head) % assistent) :
        answer +=1
    answer += ((i-head) // assistent) + 1
print(answer)

#참고사항
#(-13) % 10 = 7