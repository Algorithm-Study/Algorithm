import bisect
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for a in A:
        idx = bisect.bisect_right(B,a)
        if len(B) > idx:
            temp = B.pop(idx)
            if temp > a:
                answer += 1
        else:
            B.pop(0)
    return answer
# A를 이기지 못할 경우 가장 작은 값으로 해결해야 함
# A를 이길 경우 해당 값보다 큰 수 중 가장 작은 값을 내야 함