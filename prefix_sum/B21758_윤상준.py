n = int(input())
honeys = list(map(int, input().split()))
prefix = [honeys[0]]
result = 0
for i in range(1,n):
    prefix.append(prefix[i-1] + honeys[i])
#벌/벌/벌통
for i in range(1,n-1):
    result = max(result, prefix[n-1]*2 - prefix[0] - prefix[i] - honeys[i])
#벌/벌통/벌
for i in range(1,n-1):
    result = max(result, prefix[n-2] - prefix[i-1] + prefix[i] - prefix[0])
#벌통/벌/벌
for i in range(1,n-1):
    result = max(result, prefix[n-2] - honeys[i] + prefix[i-1])    
print(result)
# 그리디->멀리서부터 꿀 수확하는 것이 유리(단 같은 방향에서 오는 경우에는 조금 다름)