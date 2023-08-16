import bisect
n, m = map(int, input().split())
field_x = [[] for _ in range(200_000)]
field_y = [[] for _ in range(200_000)]
# 네잎클로버 위치 저장
for _ in range(n):
    y,x= map(int, input().split())
    x += 100_000
    y += 100_000
    field_x[x].append(y)
    field_y[y].append(x)
commands = list(input())
#정렬
for i in range(200_000):
    field_x[i].sort()
    field_y[i].sort()
current = [100_000,100_000]
for command in commands:
    #왼쪽
    if command == 'L':
        idx = bisect.bisect_left(field_x[current[0]], current[1])
        current = [current[0], field_x[current[0]][idx-1]]
    #오른쪽
    elif command == 'R':
        idx = bisect.bisect_right(field_x[current[0]], current[1])
        current = [current[0],field_x[current[0]][idx]]
    #위
    elif command == 'U':
        idx = bisect.bisect_right(field_y[current[1]], current[0])
        current = [field_y[current[1]][idx],current[1]]
    #아래
    else:
        idx = bisect.bisect_left(field_y[current[1]], current[0])
        current = [field_y[current[1]][idx-1],current[1]]
print(current[1]-100_000, current[0]-100_000)
# 시간초과 고려하기
# 이분탐색으로 다음 클로버 위치 찾기