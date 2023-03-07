#선택하지 않는 경우 고려시 연속해서 2개 이상 선택하지 않을 경우 1개 선택하지 않는 경우로 분해 가능 -> 점화식
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    data = []
    n = int(input().rstrip())
    for _ in range(2):
        data.append([0] + list(map(int, input().rstrip().split())))
    for i in range(2,n+1):
        data[0][i] += max(data[0][i-2], data[1][i-1], data[1][i-2])
        data[1][i] += max(data[1][i-2], data[0][i-1], data[0][i-2])
    print(max(data[0][n], data[1][n]))