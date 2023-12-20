# 초기값 설정
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 10_000
left, right = 0, max(arr)

# 최대최소의 차이가 정답보다 크면 그 이전까지 구간으로 나눔
def check(mid):
    cnt = 1
    min_val = max_val = arr[0]
    
    for i in arr:
        min_val = min(min_val, i)
        max_val = max(max_val, i)
        
        if max_val - min_val > mid:
            cnt += 1
            min_val = max_val = i
            
    return cnt

# 정답에 대한 이분탐색
while left <= right:
    mid = (left+right)//2
    
    if check(mid) <= m:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
        
print(answer)