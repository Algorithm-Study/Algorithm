n = int(input())
prefix = []
temp = 0
for _ in range(n):
    temp += int(input())
    prefix.append(temp)
result = 0
for i in range(n):
    for j in range(i+1,n):
        result = max(result, min(prefix[j]-prefix[i], temp - prefix[j] + prefix[i]))
print(result)