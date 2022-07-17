

# def Vaild():
#     global signals
#     temp = ''
#     cnt = 0
#     zero, one = 0, 0
#
#     for signal in signals:
#         temp += signal
#         if len(temp) > 1: # 두자리 수 이상이면 판단 가능
#
#             if len(temp) > 4 and signal == '0':
#                 if temp and temp.count('1') > 1:
#                     cnt += zero + one + 1
#                     temp = temp[-1]
#
#             elif temp[0] == '0':
#                 if temp == '01':
#                     cnt += 2
#                     temp =''
#                 else:
#                     return 'NO'
#
#             elif temp[0] == '1':
#
#                 if temp[-1] == '1':
#                     if len(temp) > 3:
#                         one += 1
#                     else:
#                         return 'NO'
#                 elif temp[-1] == '0':
#                     zero += 1
#
#     if cnt + len(temp) == len(signals):
#         return 'YES'


import re
import sys
sys.stdin = open('input1.txt')


T = int(input())
results = []
for tc in range(T):
    signals = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(signals):
        print("YES")
    else:
        print("NO")

