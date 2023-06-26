t = int(input())
def dfs(total, num, expression, before):
    if num <= n:
        residual = int(''.join([str(x) for x in range(num,n+1)]))
    else:
        residual = 0
    # 남은 수열로 0을 만들 수 없는 경우
    if total - residual > 0 or total + residual < 0:
        return
    # 조기 종료 조건
    if total + residual == 0 and residual != 0:
        result.append(expression + '+' + ' '.join([str(x) for x in range(num,n+1)]))
    if total - residual == 0 and residual != 0:
        result.append(expression + '-' + ' '.join([str(x) for x in range(num,n+1)]))
    # 끝까지 도달한 경우
    if num > n and total == 0:
        result.append(expression)
        return
    dfs(total+num, num+1, expression + '+' + str(num), num)
    dfs(total-num, num+1, expression + '-' + str(num), -num)
    if before < 0:
        dfs(total - before + before*10 - num, num+1, expression +' '+ str(num), -before*10 -num)
    else:
        dfs(total - before + before*10 + num, num+1, expression +' '+ str(num), before*10 + num)
for _ in range(t):
    n = int(input())
    result = []
    dfs(1,2,'1',1)
    result = sorted(list(set(result)))
    for r in result:
        print(r)
    print()
#ASCII 순서로 출력해야 함
#DFS로 진행하면 문제 해결 가능