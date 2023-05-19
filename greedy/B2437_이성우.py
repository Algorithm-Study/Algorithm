import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
target = 1

for num in arr:
    if target < num:
        break
    target += num

print(target)