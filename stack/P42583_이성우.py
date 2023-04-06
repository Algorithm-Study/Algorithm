from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    sum_bridge = 0
    truck_weights = deque(truck_weights)
    t = 0
    while truck_weights:
        if sum_bridge + truck_weights[0] <= weight:
            t += 1
            truck = truck_weights.popleft()
            bridge.appendleft(truck)
            sum_bridge += truck
            truck = bridge.pop()
            sum_bridge -= truck
        else:
            if sum_bridge - bridge[-1] + truck_weights[0] <= weight:
                t += 1
                truck = truck_weights.popleft()
                bridge.appendleft(truck)
                sum_bridge += truck
                truck = bridge.pop()
                sum_bridge -= truck
            else:
                t += 1
                bridge.appendleft(0)
                truck = bridge.pop()
                sum_bridge -= truck
        # print(bridge, truck_weights, t)
    t += bridge_length
    return t

# sum(bridge)로 bridge를 직접 더하면 tc5번이 시간초과가 됐던 문제
# 직접 더하지말고 더하고 뺀 값을 따로 받아서 현재 다리의 무게를 구하여 해결했다