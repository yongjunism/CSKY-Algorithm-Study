# 연산자 끼워넣기
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	60462	31689	20102	49.437%
# 문제
# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 
# 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 
# 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
# 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 
# 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
# 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

# 출력
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
# 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
# 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

# 예제 입력 1 
# 2
# 5 6
# 0 0 1 0
# 예제 출력 1 
# 30
# 30
# 예제 입력 2 
# 3
# 3 4 5
# 1 0 1 0
# 예제 출력 2 
# 35
# 17
# 예제 입력 3 
# 6
# 1 2 3 4 5 6
# 1-2/3+4+5*6  13002
# 2 1 1 1 # A: 0 S: 1 M: 2 D: 3
# 예제 출력 3 
# 54
# -24

N = int(input()) #N개의 숫자
answer = [] #연산자들의 순열 담을 리스트
case = list(map(int,input().split())) #1 2 3 4 5 6
ASMD = list(map(int,input().split())) #더하기 : 0 빼기 : 1 곱하기 : 2 나누기 : 3 (인덱스 기준)
tmp = [] #tmp리스트 개수가 연산자 총 개수 되면 answer에 추가

def backTraking(depth):
    if depth == N-1 : # 연산자 개수 다 채워지면 answer에 추가하기
        dc_tmp = [tmp[idx_] for idx_ in range(len(tmp))]
        answer.append(dc_tmp)
        return
    for i in range(4):
        if i== 0 and tmp.count(i)>=ASMD[0]: continue
        elif i== 1 and tmp.count(i)>=ASMD[1]: continue
        elif i== 2 and tmp.count(i)>=ASMD[2]: continue
        elif i== 3 and tmp.count(i)>=ASMD[3]: continue
        else :
            tmp.append(i)
            backTraking(depth+1)
            tmp.pop()
        
backTraking(0)

k=0
for asmd_list in answer :
    Sum = case[0]
    for idx in range(len(asmd_list)):
        if asmd_list[idx] == 0:
            Sum += case[idx+1]
        elif asmd_list[idx] == 1:
            Sum -= case[idx+1]
        elif asmd_list[idx] == 2:
            Sum *= case[idx+1]
        elif asmd_list[idx] == 3:
            if Sum < 0 : 
                Sum = -(abs(Sum) // case[idx+1])
            else : Sum //= case[idx+1]
    answer[k] = Sum
    k+=1
print(max(answer))
print(min(answer))