from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque()
    sec = 0
    while q:  # 초당 할 수 있는 일
        if len(bridge) == 0 and len(q) > 0:  # 초기 조건 bridge에 아무것도 없을 때
            truck = q.popleft()  # 트럭의 무게를 가져옴
            for i in range(truck):
                bridge.append(truck)  # 트럭을 다리 위에다가 놓아준다.

        # bridge에 뭔가 있을 때
        if len(bridge) > 0 and len(q) > 0:
            while len(q) > 0 and bridge[0] + q[0] <= weight:  # 한개 더 올려 놓을 수 있으면
                truck = q.popleft()  # 트럭의 무게를 가져옴
                for _ in range(truck):
                    bridge.append(truck)  # 트럭을 다리 위에다가 놓아준다.
            if len(q) > 0 and bridge[0] + q[0] > weight:  # 다리 위에 무게가 한도 초과일 경우
                bridge.popleft()
        else:
            bridge.popleft()
        sec += 1

    answer = 0
    return sec