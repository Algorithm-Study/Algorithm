import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    arr = list(map(int, input().split()))
    answer = 0
    max_val = 0

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            answer += max_val - arr[i]

    print(answer)