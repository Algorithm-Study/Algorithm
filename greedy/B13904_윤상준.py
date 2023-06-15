n = int(input())
homework = []
deadline = [0]*1000
for _ in range(n):
    homework.append(list(map(int, input().split())))
homework.sort(key = lambda x: -x[1])
for i in range(n):
    for j in range(homework[i][0]-1,-1,-1):
        if deadline[j] == 0:
            deadline[j] = homework[i][1]
            break
print(sum(deadline))
# 점수가 가장 큰 것부터 마감일 역순으로 탐색하면서 풀 수 있는지 체크
# 총점 계산하면 끝