import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    answer = []
    
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    if n == 1:
        first.append(0)
        second.append(0)

    answer.append([first[0], second[0]])
    answer.append([second[0] + first[1], first[0] + second[1]])

    for i in range(2, n):
        temp = []
        temp.append(max(answer[i-1][1], answer[i-2][1]) + first[i])
        temp.append(max(answer[i-1][0], answer[i-2][0]) + second[i])
        answer.append(temp)
    print(max(answer[n-1]))
    
# 문제 접근 방법
# # dp는 항상 i번째 수를 이전 항들로 어떻게 나타낼지 생각해보자
# # 이번 문제는 변이 맞닿으면 안되므로 자신의 행의 이전 요소들과는 만날 수 없다.
# # 다른 행의 요소와 만나야 하는데 2열 전의 값을 취하면 1열 전의 요소들은 선택할 수 없으므로
# # 2열 전과 1열 전의 값을 비교하여 점화식을 구할 수 있다.