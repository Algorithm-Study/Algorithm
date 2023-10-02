n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def is_end():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                return False
    return True

for _ in range(s):
    
    # 위치 정보 받기
    virus = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            virus[arr[i][j]].append((i, j))
            
    # 번호에 따른 바이러스 증식
    for idx in range(1, k+1):
        for v in virus[idx]:
            for d in range(4):
                nx, ny = v[0] + dx[d], v[1] + dy[d]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    arr[nx][ny] = idx

    # 증식이 더 진행되는지 확인
    if is_end():
        print(arr[x-1][y-1])
        break
else:
    print(arr[x-1][y-1])