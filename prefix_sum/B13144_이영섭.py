N = int(input())
data = list(map(int, input().split()))
ans = 0
start, end = 0, 0
ans_list = [0] * 1000001

while start < N and end < N:
    if not ans_list[data[end]]:
        ans_list[data[end]] = True
        end += 1
        ans += (end - start)
    else:
        ans_list[data[start]] = False
        start += 1

print(ans)
