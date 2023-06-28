n, x = map(int, input().split())
arr = list(map(int, input().split()))

s = [0]*(n+1)
for i in range(n):
    s[i+1] = s[i] + arr[i]

left = 0
right = 1
answer = float('inf')
while left < right <= n: # left <= right면 끝까지 탐색하게 된다
    if s[right] - s[left] < x:
        right += 1
    elif s[right] - s[left] >= x:
        answer = min(answer, right-left)
        left += 1
        
if answer == float('inf'):
    answer = 0
print(answer)