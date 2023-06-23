def solution(n, times):
    left = 0
    right = n*max(times)
    
    while left <= right:
        mid = (left+right)//2
        tmp = 0
        for t in times:
            tmp += mid//t
        if tmp >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left