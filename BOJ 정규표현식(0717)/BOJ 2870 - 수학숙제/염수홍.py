import sys
sys.stdin = open('input1.txt')

# 숫자를 모두 찾은 후에 오름차순 정렬 (sort())
results = []
N = int(input())

# 0이 앞에 나올경우 생략 가능

cnt = 0
for _ in range(N):
     words = input()
     temp = ''
     for idx in range(len(words)):
         if words[idx].isdigit(): # 만약에 숫자라면 ~
                temp += words[idx]
         else: # 문자가 등장 !
            if temp:
                results.append(int(temp))
                temp = ''
                cnt = 0
     if temp:
        results.append(int(temp))

results.sort()
for result in results:
    print(result)