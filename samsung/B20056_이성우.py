def move_fire(arr):
    # 파이어볼 움직인 뒤 임시 배열에 배치 후 반환
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                for m, s, d in arr[i][j]:
                    tmp[(i + s*direction[d][0]) % n][(j + s*direction[d][1]) % n].append([m, s, d])
                    
    return tmp

def divide_fire(arr):
    # 파이어볼이 2개 이상 같이 있으면 조건에 따라 분할
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) >= 2:
                mass = speed = 0
                odd_cnt = 0
                for m, s, d in arr[i][j]:
                    mass += m
                    speed += s
                    if d%2 == 1:
                        odd_cnt += 1
                mass = mass//5
                speed = speed//len(arr[i][j])
                if mass == 0:
                    arr[i][j] = []
                else:
                    if odd_cnt == len(arr[i][j]) or odd_cnt == 0:
                        arr[i][j] = [[mass, speed, i] for i in [0, 2, 4, 6]]
                    else:
                        arr[i][j] = [[mass, speed, i] for i in [1, 3, 5, 7]]
    
    return arr

# 초기값 설정
n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1],
             [1, 0], [1, -1], [0, -1], [-1, -1]]

# r, c, m, s, d
# (r, c): 좌표, m: 질량, s: 속력, d: 방향
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

for _ in range(k):
    arr = move_fire(arr)
    arr = divide_fire(arr)
    
answer = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            for m, s, d in arr[i][j]:
                answer += m
                
print(answer)