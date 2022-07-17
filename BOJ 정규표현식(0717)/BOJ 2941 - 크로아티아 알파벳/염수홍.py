import sys
sys.stdin = open('input1.txt')

words = input()
Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 01 23 45 67

temp = ''
cnt = 0

for i in range(len(words)):
    temp += words[i]
    if len(temp) > 1 and temp in Croatia: # 2글자이면서 ~~인경우
        cnt += 1
        temp = ''
    elif len(temp) > 1:
        if temp == 'dz':
            pass
        else:
            cnt += 1
            temp = temp[1:] # 앞에 한글자 지워줌
            if len(temp) > 1:
                cnt += 1
                temp = temp[-1]

if len(temp) > 0:
    if temp in Croatia:
        cnt += 1
    else:
        cnt += len(temp)
print(cnt)

