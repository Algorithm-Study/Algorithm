import sys
input = sys.stdin.readline

cost = []

N = int(input())

for i in range(N):
    ls = list(map(int, input().split()))
    cost.append(ls)

pay = []
tmp = []
for i in range(3):
    tmp.append(cost[0][i])
pay.append(tmp)

for i, ls in enumerate(cost[1:]):
    temp = []
    temp.append(min(pay[i][1], pay[i][2]) + ls[0])
    temp.append(min(pay[i][0], pay[i][2]) + ls[1])
    temp.append(min(pay[i][0], pay[i][1]) + ls[2])
    pay.append(temp)

print(min(pay[N-1]))

# 문제 접근 방식
# # N이 1000이므로 완탐으로는 불가능
# # 이전 집의 색과 다르다는 것으로 규칙 찾기 가능
# # min(이전 집 다른색1, 이전 집 다른색2) + 이번 집 현재 색
# 새로 배운 python
# # list를 묶어서 넣어야 2차원 list이다.
# # c++의 2차원 배열과 헷갈린다. 잘 기억하자.