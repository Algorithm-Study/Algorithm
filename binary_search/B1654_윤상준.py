n, k = map(int, input().split())
cables = [int(input()) for _ in range(n)]
maximum = max(cables)
def binary_search(cables, start, end):
    while start <= end:
        mid = (start + end)//2
        count = 0
        for cable in cables:
            count += cable//mid
        if count >= k:
            start = mid + 1
        else:
            end = mid  - 1
    return end

answer = binary_search(cables, 1, maximum)
print(answer)
# 자르려는 케이블 길이를 기준으로 이분탐색 진행하면 됨