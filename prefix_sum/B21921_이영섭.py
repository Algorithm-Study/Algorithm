N, X = map(int, input().split())
data = list(map(int, input().split()))
sum = 0
for i in range(X):
    sum += data[i]
max_sum = sum
length = 1
for i in range(X, N):
    sum = sum + data[i] - data[i-X]
    if sum > max_sum:
        max_sum = sum
        length = 1
    elif sum == max_sum:
        length += 1
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(length)