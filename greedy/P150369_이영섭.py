def solution(cap, n, deliveries, pickups):
    answer = 0
    dm, pm = -1, -1
    # 마지막 번호 확인
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0:
            dm = i
            break
    for i in range(n-1, -1, -1):
        if pickups[i] != 0:
            pm = i
            break
    # 배달할 물건이나 가져올 물건이 남아 있는 동안
    while dm > -1 or pm > -1:
        dm_sample, pm_sample = 0, 0
        while deliveries[dm] == 0 and dm > -1:
            dm -= 1
        while pickups[pm] == 0 and pm > -1:
            pm -= 1
        distance = pm+1 if pm > dm else dm+1
        # 가장 멀리 있는 것부터 배달 및 수거
        while dm > -1 and dm_sample < cap:
            if dm_sample + deliveries[dm] > cap:
                deliveries[dm] -= cap - dm_sample
                dm_sample = cap
                break
            else:
                dm_sample += deliveries[dm]
                deliveries[dm] = 0
                dm -= 1
        while pm > -1 and pm_sample < cap:
            if pm_sample + pickups[pm] > cap:
                pickups[pm] -= cap - pm_sample
                pm_sample = cap
                break
            else:
                pm_sample += pickups[pm]
                pickups[pm] = 0
                pm -= 1
        answer += distance * 2
    
    return answer