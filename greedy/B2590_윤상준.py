papers = [int(input()) for _ in range(6)]
answer = 0
# 길이가 6인 경우
if papers[5]:
    answer += papers[5]
# 길이가 5인 경우
if papers[4]:
    answer += papers[4]
    papers[0] = max(0, papers[0]- 11 * papers[4])
#print(papers)
# 길이가 4인 경우
while papers[3]:
    papers[3] -= 1
    temp = min(papers[1],5)
    papers[1] = max(0, papers[1] - 5)
    if temp < 5:
        papers[0] = max(0, papers[0] - 4 * (5 - temp))
    answer += 1
#print(papers)
# 길이가 3인 경우
while papers[2]:
    area = 36 - 9 * min(papers[2], 4)
    if papers[2] == 3:
        area -= min(papers[1], 1) * 4
        papers[1] = max(0, papers[1]- 1)
    elif papers[2] == 2:
        area -= min(papers[1], 3) * 4
        papers[1] = max(0, papers[1]-3)
    elif papers[2] == 1:
        area -= min(papers[1], 5) * 4
        papers[1] = max(0, papers[1]-5)
    papers[2] = max(0, papers[2] - 4)
    papers[0] = max(0, papers[0] - area)
    answer += 1
while papers[1]:
    area = 36 - 4 * min(papers[1], 9)
    papers[1] = max(0, papers[1]- 9)
    papers[0] = max(0, papers[0] - area)
    answer += 1
while papers[0]:
    papers[0] = max(0, papers[0] - 36)
    answer += 1
print(answer)