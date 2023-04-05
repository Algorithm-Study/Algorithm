n, m, l, k = map(int,input().split())

stars = []
for _ in range(k):
    x, y = map(int, input().split())
    stars.append([x, y])

# print(stars)
answer = 0
for u in range(k):
    for v in range(k):
        x1 = stars[u][0]
        y1 = stars[v][1]
        x2 = x1 + l
        y2 = y1 + l
        tmp = 0
        for w in range(k):
            if x1 <= stars[w][0] <= x2 and y1 <= stars[w][1] <= y2:
                tmp += 1
                
        answer = max(answer, tmp)

print(k-answer)

# 배열을 만들지 않고 별들 좌표를 기준으로 트램펄린을 배치하여 최대값을 탐색한다
# 한 쪽만 탐색해도 되는 이유는 오른쪽 기준으로 탐색하는 것과 왼쪽으로 탐색하는 것이 서로 중복되기 때문에
# 한 쪽으로만 탐색해도 모든 경우의 수를 탐색할 수 있다