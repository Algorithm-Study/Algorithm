from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    time = deque()
    idx = 0
    while True:
        answer += 1
        for i in range(len(time)):
            time[i] += 1
        if bridge_length in time:
            bridge.popleft()
            time.popleft()
        if len(bridge) < bridge_length and idx < len(truck_weights):
            if sum(bridge) + truck_weights[idx] <= weight:
                bridge.append(truck_weights[idx])
                time.append(0)
                idx += 1
        if idx == len(truck_weights) and not bridge:
            break
        #print(bridge)
    return answer