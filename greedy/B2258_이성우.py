import sys
input = sys.stdin.readline

# 초기값 설정
n, m = map(int, input().split())
arr = []
for _ in range(n):
    weight, price = map(int, input().split())
    arr.append((price, weight))
arr.sort(key=lambda x: (x[0], -x[1]))
answer = -1
weight, same = 0, 0

# 고기 탐색
for i in range(n):
    weight += arr[i][1]
    
    # 현재 고기가 이전 고기와 가격이 같은 경우
    if i >= 1 and arr[i][0] == arr[i-1][0]:
        same += arr[i][0]
    else:
    # 현재 고기가 이전 고기보다 가격이 더 비싼 경우
        same = 0
    if weight >= m:
        answer = min(answer if answer != -1 else sys.maxsize, arr[i][0]+same)

print(answer)