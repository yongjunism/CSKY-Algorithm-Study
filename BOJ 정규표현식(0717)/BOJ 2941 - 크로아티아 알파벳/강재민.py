# case = input()
# cnt = 0
# i = 0

# while i < len(case) :
#     if case[i] == 'c' and len(case)-i>1:
#         if case[i+1] == '=':
#             cnt += 1
#             i+=2
#         elif case[i+1] == '-':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
#     elif case[i] == 'd' and len(case)-i>1:
#         if len(case)-i>2 and case[i+1:i+3] == 'z=':
#             cnt += 1
#             i+=3
#         elif case[i+1] == '-':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
    
#     elif case[i] == 'l' and len(case)-i>1:
#         if case[i+1] == 'j':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
#     elif case[i] == 'n' and len(case)-i>1:
#         if case[i+1] == 'j':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
#     elif case[i] == 's' and len(case)-i>1:
#         if case[i+1] == '=':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
#     elif case[i] == 'z' and len(case)-i>1:
#         if case[i+1] == '=':
#             cnt += 1
#             i+=2
#         else : cnt +=1; i+=1
#     else : cnt+=1;i+=1
    
# print(cnt)
        
# #a=input();print(len(a)-sum(map(a.count,['-','=','lj','nj','dz='])))


import re

case = input()
p = re.compile('c=|c-|dz=|d-|lj|nj|s=|z=')

result = p.sub('0',case)
print(len(result))