N = int(input()) # 시험장의 개수
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for a in A:
    students = a
    if students - B <= 0 : # 총감독관 한명으로 되면
        cnt += 1 # 총감독관 한명만 더해주고 넘어감
    else: # 부감독관이 필요할 경우
        students -= B
        cnt += 1
        if students%C > 0: # 부감독관이 있고 그 이후로 나머지가 있는 경우
            cnt += (students//C) +1 # 1을 더해줌 나머지만큼
        else: # 부감독관이 딱 떨어지는 경우
            cnt += (students//C)  #몫을 넣어줌 +

print(cnt)