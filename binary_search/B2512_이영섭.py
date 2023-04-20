N = int(input())
data = list(map(int, input().split()))
M = int(input())

low = 1
high = max(data)
max_sum = 0
while low <= high:
    mid = (low + high) // 2
    sum = 0
    for da in data:
        if da < mid:
            sum += da
        else:
            sum += mid
    if sum > max_sum and sum <= M:
        max_sum = sum
        ans = mid
    if sum < M:
        low = mid + 1
    elif sum > M:
        high = mid - 1
    else:
        ans = mid
        break
print(ans)

# 문제 접근 방법
# # 최적화 문제는 결정문제로 변경할 수 있다.
# # '가장 좋은 답은 무엇인가?'라는 최적화 문제를 'x 혹은 그보다 좋은 답이 있는가?'라는 결정문제로 변형