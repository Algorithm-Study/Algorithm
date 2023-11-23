import heapq
import sys
input = sys.stdin.readline

# 초기값 설정
n = int(input())
greater_than_one = []
less_than_one = []
answer = 0

# 1을 기준으로 분류
for _ in range(n):
    num = int(input())
    if num > 1:
        heapq.heappush(greater_than_one, -num)
    elif num == 1:
        answer += 1
    else:
        heapq.heappush(less_than_one, num)

def cal(arr):
    '''
    두 개씩 짝지어서 합산
    '''
    cnt = 0
    while len(arr) > 1:
        num1, num2 = heapq.heappop(arr), heapq.heappop(arr)
        cnt += num1*num2
    return cnt, arr


# 큰 수부터 두 개씩 짝 지어서 곱
tmp, arr = cal(greater_than_one)
# 양수의 최대힙이라 음수로 빼서 합산
answer += tmp - sum(arr)

# 작은 수부터 두 개씩 짝 지어서 곱
tmp, arr = cal(less_than_one)
# 음수의 최소힙이라 양수로 더해서 합산
answer += tmp + sum(arr)

print(answer)