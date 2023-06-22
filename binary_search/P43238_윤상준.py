def solution(n, times):
    start, end = 1, max(times)*n
    while start <= end:
        mid = (start + end)//2
        temp = 0
        for time in times:
            temp += mid // time
        if temp >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start
# 이분 탐색으로 총 걸리는 시간을 정하면 되는 문제