n = int(input())
idx = list(map(int, input().split()))
answer = []
for i, val in enumerate(idx[::-1]):
    answer.insert(val,n-i)

print(*answer)