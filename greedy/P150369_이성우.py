def solution(cap, n, deliveries, pickups):
    deli = 0
    pick = 0
    answer = 0
    for i in reversed(range(n)):
        deli += deliveries[i]
        pick += pickups[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += i+1
            
    return answer*2