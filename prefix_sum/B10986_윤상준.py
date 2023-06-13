n, m = map(int, input().split())
data = list(map(int, input().split()))
remain = [0]*m
remain[0] = 1
total = 0
for i in range(n):
    total += data[i]
    remain[total%m] +=1
result = 0
for i in range(m):
    result += remain[i] * (remain[i]-1) // 2
print(result)
# 나머지가 같은 것들을 선택해서 0을 만들면 되는 문제
# 하나만 선택해도 0이 되는 경우는 나누어떨어질 때만 해당
# 따라서 0인 경우에 경우의 수 한가지 추가해야 해결 가능