t = int(input())
for _ in range(t):
    n = int(input())
    calls = sorted([input() for _ in range(n)])
    flag = 1
    for i in range(n-1):
        if calls[i+1].startswith(calls[i]):
            print('NO')
            break
    else:
        print('YES')
# 정렬된 상태이므로 현재 위치에서 오른쪽 값이 해당 문자로 시작하는지 확인하면 됨
# 다 확인하게 되면 시간 초과