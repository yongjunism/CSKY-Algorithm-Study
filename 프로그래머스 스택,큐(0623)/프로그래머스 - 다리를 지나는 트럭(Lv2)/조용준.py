from collections import deque
def solution(bridge_length, weight, truck_weights):
    sec = 0
    bridge = deque([0 for _ in range(bridge_length)])
    while bridge:
        bridge.popleft()
        sec += 1
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return sec