N = int(input())
ball = [[idx]+list(map(int, input().split())) for idx in range(N)]
new_ball = sorted(ball, key=lambda x: x[2], reverse=True)
prefix_sum, ans = [0]*(N+1), [0]*(N+1)
j, ball_val = N-1, 0
# print(new_ball)
for i in range(N-1, -1, -1):
    # print(i, prefix_sum)
    while new_ball[j][2] < new_ball[i][2]:
        # print('hi', j, new_ball[j], i, new_ball[i])
        prefix_sum[new_ball[j][1]] += new_ball[j][2]
        ball_val += new_ball[j][2]
        j -= 1
    ans[new_ball[i][0]] = ball_val - prefix_sum[new_ball[i][1]]
for i in range(N):
    print(ans[i])
# print(ans)