# 조건에 맞게 구현하면 끝
t = int(input())
for _ in range(t):
    n,k,id,m = map(int, input().split())
    # -3 : 제출 횟수, -2: 최근 제출 -1: 총점
    log = [[x+1]+[0]*(k+3) for x in range(n)]
    for i in range(1,m+1):
        submit, question, score =  map(int, input().split())
        if log[submit-1][question] < score:
            log[submit-1][-1] += score - log[submit-1][question]
            log[submit-1][question] = score
        log[submit-1][-3] += 1
        log[submit-1][-2] = i
    log.sort(key = lambda x: (-x[-1], x[-3], x[-2]))
    print(log)
    for i in range(n):
        if log[i][0] == id:
            print(i+1)
            break