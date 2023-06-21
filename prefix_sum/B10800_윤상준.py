n = int(input())
color = [0]*2_000_001
balls = []
for i in range(n):
    balls.append(list(map(int, input().split()))+[i])
balls.sort(key= lambda x : (x[1], x[0]))
total = 0
idx, s_idx = 0,0
result = [0]*(n)
while idx < n:
    ball = balls[idx]
    s_ball = balls[s_idx]
    while ball[1] > s_ball[1]:
        total += s_ball[1]
        color[s_ball[0]] += s_ball[1]
        if s_idx == n-1:
            break
        s_idx += 1
        s_ball = balls[s_idx]
    result[ball[2]] = total - color[ball[0]]
    idx += 1
for i in range(n):
    print(result[i])
# 정렬 순으로 넣으면서 조건에 맞게 각 공별 점수를 기록한 뒤 출력하면 끝