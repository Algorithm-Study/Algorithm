import heapq

n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

null = []
for i in range(1, len(arr)):
    heapq.heappush(null, -(arr[i]-arr[i-1]))

left, right = 1, -null[0]

# 휴게소 사이에 일정한 거리를 기준으로 휴게소를 설치한 후
# 휴게소 거리간의 최대값을 기준으로 영역 탐색
while left <= right:
    mid = (left + right)//2
    cnt = m
    tmp_null = [_ for _ in null]
    
    # m 개의 휴게소 설치
    while cnt:
        num = heapq.heappop(tmp_null) # num 음수
        
        # 휴게소 사이의 최대값에 mid 거리를 설치할 수 없다면
        # 설치 거리를 줄인다
        if num+mid >= 0:
            right = mid - 1
            break
        
        # mid 거리만큼 설치하고 영역 분리
        heapq.heappush(tmp_null, num+mid) # 음수
        heapq.heappush(tmp_null, -mid) # 음수
        cnt -= 1

    # 휴게소 사이 거리의 최대값이 mid 기준 거리보다 크면
    # 더 크게 자를 수 있고
    # mid 거리 보다 같거나 작으면 더 작은 영역 탐색
    num = heapq.heappop(tmp_null)
    if mid < -num:
        left = mid + 1
    else:
        right = mid - 1

# 휴게소 사이 거리의 최대값의 최소값을 반환해야 하므로 left 반환
print(left)
        