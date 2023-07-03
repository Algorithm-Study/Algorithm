import sys
input = sys.stdin.readline

n = int(input().rstrip())

num_list = list(map(int, input().split()))

answer = 0
start, end = 0, 0
arr = [False for _ in range(1000001)]
while start < n and end < n:
    if not arr[num_list[end]]:
        arr[num_list[end]] = True
        end += 1
        answer += end - start
    else:
        arr[num_list[start]] = False
        start += 1

print(answer)