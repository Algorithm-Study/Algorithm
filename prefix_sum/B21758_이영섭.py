N = int(input())
honey = list(map(int, input().split()))
temp, ans, sum_honey = honey[0], 0, sum(honey)
for i in range(1, N):
    temp += honey[i]
    ans = max(ans, sum_honey - honey[0] + sum_honey - temp - honey[i])
temp = honey[-1]
for i in range(N-2, 0, -1):
    temp += honey[i]
    ans = max(ans, sum_honey - honey[-1] + sum_honey - temp - honey[i])
for i in range(1, N):
    ans = max(ans, sum_honey + honey[i] - honey[0] - honey[-1])
print(ans)