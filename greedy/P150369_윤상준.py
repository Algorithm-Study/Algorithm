# 가장 먼 거리에 있는 곳부터 제거하면서 진행하되 배달 먼저 진행 후 수거
def solution(cap, n, deliveries, pickups):
    new_deliveries = deliveries[::-1]
    new_pickup = pickups[::-1]
    length = 0
    d_stack = 0
    p_stack = 0
    for i in range(n):
        d_stack += new_deliveries[i]
        p_stack += new_pickup[i]
        while d_stack > 0 or p_stack > 0:
            d_stack -= cap
            p_stack -= cap
            length += (n-i)*2
    return length