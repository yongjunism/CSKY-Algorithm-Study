import sys
sys.stdin = open('input1.txt')

words = input()
check = input()
C = len(check)

temp = ''
cnt = 0
for word in words:
    temp += word
    if C == len(temp): # 같은 길이가 됐을 때
        if temp == check: # 같으면
            cnt += 1
            temp = ''
        else: # 같지 않다면
            temp = temp[1:] # 앞에 한자리 잘라줌

print(cnt)
