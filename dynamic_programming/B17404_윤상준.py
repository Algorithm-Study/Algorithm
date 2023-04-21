# RGB 거리 문제에서 조건 추가 -> 1번과 N번 집이 같지 않아야 함!
# 1번에 무엇을 골랐는지 확정한 상태에서 DP 계산해서 최솟값 구하기
n = int(input())
INF = 1_000_001
coloring = [list(map(int, input().split())) for _  in range(n)]
min_coloring = 1_000_001
for k in range(3):
    temp = [[INF]*3 for _ in range(n)]
    temp[0][k] = coloring[0][k]
    for i in range(1,n):
        for j in range(3):
            temp[i][j] = coloring[i][j] + min([temp[i-1][x] if x!=j else INF for x in range(3)])
    min_coloring = min([temp[-1][x] if x!=k else INF for x in range(3)] + [min_coloring])
print(min_coloring)