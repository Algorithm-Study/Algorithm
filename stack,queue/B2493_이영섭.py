N = int(input())
top = list(map(int, input().split()))
ans = [0] * N
temp = []

for idx, tp in enumerate(top):
    if idx == 0:
        temp.append((idx, tp))
    if temp[-1][1] <= tp:
        while temp and temp[-1][1] <= tp:
            temp.pop()
        if len(temp):
            ans[idx] = temp[-1][0] + 1
        temp.append((idx, tp))
    else:
        ans[idx] = temp[-1][0] + 1
        temp.append((idx, tp))

for an in ans:
    print(an, end=" ")

# 문제 접근 방법
# # temp라는 list를 스택으로 활용해 기존 값보다 작은 값들은 쌓이고 큰 값들은 제거하고 쌓이도록 하여 해결