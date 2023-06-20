n,m,h = map(int, input().split())
ladder = [[0 for _ in range(n+1)] for _ in range(h+1)]
result = []
possible = []
for _ in range(m):
    x,y = map(int, input().split())
    ladder[x][y] = 1
# 다리 놓을 수 있는 영역 확인
for i in range(1,h+1):
    for j in range(1,n):
        if not(ladder[i][j-1] or ladder[i][j] or ladder[i][j+1]):
            possible.append((i,j))
# 순차적으로 계산했을 때 laddar의 시작과 끝이 동일한지 비교
def check_laddar() ->int:
    for i in range(1,n+1):
        current = i
        for j in range(1,h+1):
            if ladder[j][current]:
                current += 1
            elif ladder[j][current - 1]:
                current -= 1
        if current != i:
            return 0
    return 1

def dfs(added, start) -> None:
    #사다리가 4개 놓인 경우 제외
    if added >= 4:
        return
    # 조건을 만족하면 결과 삽입 후 종료                
    if check_laddar():
        result.append(added)
        return
    for p in range(start, len(possible)):
        x,y = possible[p]
        # 다리 놓을 수 있는지 체크
        if not (ladder[x][y-1] or ladder[x][y+1]):
            ladder[x][y] = 1
            dfs(added+1, p+1)
            ladder[x][y] = 0
dfs(0,0)
if result:
    print(min(result))
else:
    print(-1)
# 다리 존재 여부를 확인하는 리스트 사이즈를 1씩 늘려서 푸는 것이 더 편함
# 시작과 끝이 같지 않은 경우 다리를 놓도록 설정하여 재귀적으로 반복하면 됨