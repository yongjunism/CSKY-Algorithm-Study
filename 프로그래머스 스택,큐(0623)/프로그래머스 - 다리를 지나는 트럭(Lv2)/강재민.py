from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    bridge = deque()
    while True:
        if truck_weights:
            if bridge and sum(list(map(lambda x: x[1],bridge))) + truck_weights[0] <= weight :
                tmp = [bridge_length,truck_weights.popleft()]
                bridge.append(tmp)
            elif not bridge:
                tmp = [bridge_length,truck_weights.popleft()]
                bridge.append(tmp)
        answer +=1
        for i in bridge: i[0] -=1
        bridge = list(filter(lambda x: x[0] != 0,bridge))
        if not bridge and not truck_weights: break
    return answer