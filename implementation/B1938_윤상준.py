from collections import deque
way = [(-1,-1), (-1,0),(-1,1),(0,-1), (0,0),(0,1),(1,-1), (1,0),(1,1)]
n = int(input())
tree, goal = [], []
field = []
# 입력 받기
for i in range(n):
    line = list(input())
    for j in range(n):
        if line[j] == 'B':
            tree.append((i,j))
            line[j] = '0'
        elif line[j] == 'E':
            goal.append((i,j))
            line[j] = '0'
    field.append(line)
tree.sort(key = lambda x : (x[0], x[1]))
goal.sort(key = lambda x : (x[0], x[1]))
queue = deque()
queue.append((tree, 0))
visited = set()
visited.add(tuple(tree))
while queue:
    current, cnt = queue.popleft()
    # 도착지점에 도착한 경우
    if sorted(current, key = lambda x : (x[0],x[1])) == goal:
        print(cnt)
        break
    # 위로 이동
    temp = []
    for cx,cy in current:
        ncx, ncy = cx-1, cy
        # 범위 내에 존재하고 이동 위치에 나무가 없는 경우 이동 가능
        if ncx < 0 or ncy < 0 or ncx >= n or ncy >= n or field[ncx][ncy] != '0':
            break
        temp.append((ncx,ncy)) 
    else:
        # 방문한 적이 없는 경우
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            queue.append((temp, cnt + 1))
    # 아래로 이동
    temp = []
    for cx,cy in current:
        ncx, ncy = cx+1, cy
        # 범위 내에 존재하고 이동 위치에 나무가 없는 경우 이동 가능
        if ncx < 0 or ncy < 0 or ncx >= n or ncy >= n or field[ncx][ncy] != '0':
            break
        temp.append((ncx,ncy)) 
    else:
        # 방문한 적이 없는 경우
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            queue.append((temp, cnt + 1))
    # 왼쪽으로 이동
    temp = []
    for cx,cy in current:
        ncx, ncy = cx, cy-1
        # 범위 내에 존재하고 이동 위치에 나무가 없는 경우 이동 가능
        if ncx < 0 or ncy < 0 or ncx >= n or ncy >= n or field[ncx][ncy] != '0':
            break
        temp.append((ncx,ncy)) 
    else:
        # 방문한 적이 없는 경우
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            queue.append((temp, cnt + 1))
    # 오른쪽으로 이동
    temp = []
    for cx,cy in current:
        ncx, ncy = cx, cy+1
        # 범위 내에 존재하고 이동 위치에 나무가 없는 경우 이동 가능
        if ncx < 0 or ncy < 0 or ncx >= n or ncy >= n or field[ncx][ncy] != '0':
            break
        temp.append((ncx,ncy)) 
    else:
        # 방문한 적이 없는 경우
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            queue.append((temp, cnt + 1))
    # 회전
    temp = []
    for cx,cy in current:
        # 범위 안에 나무가 있으면 불가능
        for i in range(9):
            nx,ny = current[1][0] + way[i][0], current[1][1] + way[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or field[nx][ny] == '1':
                break
        # 회전이 가능한 경우
        else:
            if [cx,cy] == current[1]:
                temp.append([ncx,ncy])
                continue
            ncx, ncy = current[1][0] + (cy - current[1][1]), current[1][1] + (cx - current[1][0])
            # 범위 내에 존재하고 이동 위치에 나무가 없는 경우 이동 가능
            if ncx < 0 or ncy < 0 or ncx >= n or ncy >= n or field[ncx][ncy] != '0':
                break
            temp.append((ncx,ncy)) 
    else:
        # 방문한 적이 없는 경우
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            queue.append((temp, cnt + 1))
    
else:
    print(0)
    
# 방문 처리에 대해서 고민해야 하는 문제 -> 3차원 리스트 or 집합 중에서 집합 선택해서 문제 해결
