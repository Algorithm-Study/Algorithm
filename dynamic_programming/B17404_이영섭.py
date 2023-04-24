N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 1e8
for first in range(3):
    paint = [[1e8] * 3 for _ in range(N)]
    paint[0][first] = data[0][first]
    for i in range(1, N):
        paint[i][0] = min(paint[i - 1][1], paint[i - 1][2]) + data[i][0]
        paint[i][1] = min(paint[i - 1][0], paint[i - 1][2]) + data[i][1]
        paint[i][2] = min(paint[i - 1][0], paint[i - 1][1]) + data[i][2]
    for last in range(3):
        if first != last:
            ans = min(ans, paint[-1][last])
print(ans)

# 문제 접근 방법
# # RGB거리1과 다른 점은 순환이라는 것
# # 따라서 한 번의 dp로는 풀리지 않고 시작점을 정해놓고
# # 총 세 번의 dp를 진행해야 해결할 수 있다.