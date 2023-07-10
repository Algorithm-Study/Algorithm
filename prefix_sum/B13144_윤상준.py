n = int(input())
sequence = list(map(int, input().split()))
result, start, end = 0,0,0
visited = [0]*100_001
while start < n and end < n:
    if not visited[sequence[end]]:
        visited[sequence[end]] = True
        end += 1
        result += end - start
    else:
        visited[sequence[start]] = False
        start += 1
print(result)
# 모든 수열은 해당 위치에서 앞의 부분수열만 고려
# 만나지 않은 값인 경우 end 인덱스 증가
# 이미 포함된 수가 등장한 경우 반복된 수를 제거하기 전까지 계속 제거(start 인덱스 증가)
