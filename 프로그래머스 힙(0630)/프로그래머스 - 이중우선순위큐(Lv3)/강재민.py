import heapq
def solution(operations):
    numbers=[]
    for operator in operations:
        
        alp,num = operator.split()
        
        if alp == 'I':
            heapq.heappush(numbers,int(num))
        elif alp == 'D':
            if numbers:
                if int(num) == -1:
                    heapq.heappop(numbers)
                if int(num) == 1:
                    numbers = heapq.nlargest(len(numbers),list(numbers))[1:]
                    heapq.heapify(numbers)
    if list(numbers):
        return [max(numbers),min(numbers)]
    else : return [0,0]