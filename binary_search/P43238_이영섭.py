def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n
    while left < right:
        mid = (left + right) // 2
        check = 0
        for t in times:
            check += mid // t
            if check >= n:
                break
        if check >= n:
            right = mid
            answer = mid
        else:
            left = mid + 1
    return answer
