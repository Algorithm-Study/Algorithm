import sys
def solution(stones, k):
    answer = sys.maxsize
    for i in range(len(stones)-k+1):
        answer = min(answer, max(stones[i:i+k]))
    return answer
# Sliding Window 방식으로는 효율성 체크에서 시간초과 발생
def solution(stones, k):
    start,end = 1, max(stones)
    while start <= end:
        mid =(start + end)//2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt >= k:
                    end = mid -1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start
# 이분탐색으로 정답을 찾아야 효율성 통과 가능