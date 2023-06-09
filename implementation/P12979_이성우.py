from typing import List
import math
def solution(n: int, stations: List[int], w: int) -> int:
    answer = 0
    stations.append(n+w+1)
    left = 1
    for s in stations:
        right = s-w
        answer += math.ceil((right - left)/(1+w*2))
        left = s+w+1
        
    return answer