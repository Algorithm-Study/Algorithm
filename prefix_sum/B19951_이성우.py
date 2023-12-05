import sys
input = sys.stdin.readline

# 초기값 설정
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]*(n+1)

# 누적합 표기
for _ in range(m):
    a, b, k = map(int, input().split())
    prefix_sum[a-1] += k
    prefix_sum[b] -= k

# 누적합에 따른 결과 출력
cnt = 0
for i in range(n):
    cnt += prefix_sum[i]
    print(arr[i]+cnt, end=" ")