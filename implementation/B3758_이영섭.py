T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    data = [[0]*k for _ in range(n)]
    count = [0]*n
    time = [0]*n
    for idx in range(m):
        i, j, s = map(int, input().split())
        i, j = i - 1, j - 1
        if data[i][j] < s:
            data[i][j] = s
        count[i] += 1
        time[i] = idx
    sort_list = [[sum(data[i]), count[i], time[i], i] for i in range(n)]
    sort_list.sort(key=lambda x: [-x[0], x[1], x[2]])
    for idx, sl in enumerate(sort_list):
        if sl[3] == t-1:
            print(idx+1)
            break

# 문제 접근 방법
# # 조건에 맞춰서 정렬의 key 값을 설정할 수 있는지가 중요하다.