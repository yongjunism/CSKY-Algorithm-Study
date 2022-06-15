from collections import deque
gear = [deque(map(int,input())) for _ in range(4)]
gear = [deque([0,0,0,0,0,0,0,0])] + gear

N = int(input())
gear_rotate = [list(map(int,input().split())) for _ in range(N)]


def check_left(gear_number,direction):
    global will_change_list
    if gear_number == 1: return
    if gear[gear_number][6] == gear[gear_number-1][2]:
        return
    else:
        will_change_list.append((gear_number-1,-direction))
        check_left(gear_number-1,-direction)
        
def check_right(gear_number,direction):
    global will_change_list
    if gear_number == 4: return
    if gear[gear_number+1][6] == gear[gear_number][2]:
        return
    else:
        will_change_list.append((gear_number+1,-direction))
        check_right(gear_number+1,-direction)

def change_list_rotate():
    for i in will_change_list:
        gear[i[0]].rotate(i[1])

for i in gear_rotate :
    will_change_list = deque([(i[0],i[1])])
    #i[0]은 기어의 인덱스
    check_left(i[0],i[1])
    check_right(i[0],i[1])
    change_list_rotate()

answer = 0  
for i in range(1,5):
    if gear[i][0] == 1:
        answer += 2**(i-1)
print(answer)