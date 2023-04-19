N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cash = [0] + list(map(int, input().split()))
ans = sum(cash)
data = [[0]*(sum(cash)+1) for _ in range(N+1)]
for i in range(1, N+1):
    mem = memory[i]
    cas = cash[i]
    for j in range(1, sum(cash)+1):
        if j < cas:
            data[i][j] = data[i-1][j]
        else:
            data[i][j] = max(mem + data[i-1][j-cas], data[i-1][j])
        if data[i][j] >= M:
            ans = min(ans, j)
if M != 0:
    print(ans)
else:
    print(0)
    
# 문제 접근 방법
# # i번째 앱을 종료할 것인가 아닐 것인가로 고민했으나 답이 나오지 않음
# # 가방문제 유형이므로 cost가 C일 때, 얼마나 많은 메모리를 확보할 수 있냐?
# # 의 문제로 바꾸어 접근한다면 해결할 수 있다.
# # 종료된 메모리가 M보다 크다면 그 중에서 가장 작은 cost의 값을 출력한다.