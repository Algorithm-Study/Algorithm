import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rsplit())
arr = [int(input().rstrip()) for _ in range(n)]
left, right = 0, 0
answer = 0

while left != n:
    right = left + k
    nums = set()
    flag = True
    for i in range(left, right):
        i %= n
        nums.add(arr[i])
        if arr[i] == c:
            flag = False

    cnt = len(nums)
    if flag:
        cnt += 1
    answer = max(answer, cnt)
    left += 1

print(answer)