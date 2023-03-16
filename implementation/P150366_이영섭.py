pyo = [[[i, j] for j in range(51)] for i in range(51)]
value = [['EMPTY' for _ in range(51)] for i in range(51)]

def find_parent(x, y):
    if pyo[x][y] == [x, y]:
        return pyo[x][y]
    pyo[x][y] = find_parent(pyo[x][y][0], pyo[x][y][1])
    return pyo[x][y]

def union_parent(r1, c1, r2, c2):
    r1, c1 = find_parent(r1, c1)
    r2, c2 = find_parent(r2, c2)
    
    if r1 == r2 and c1 == c2:
        return
    if value[r1][c1] == 'EMPTY':
        pyo[r1][c1] = [r2, c2]
    else:
        pyo[r2][c2] = [r1, c1]

def solution(commands):
    answer = []
    for com in commands:
        temp = com.split()
        if temp[0] == "UPDATE" and len(temp) == 4:
            x, y = find_parent(int(temp[1]), int(temp[2]))
            value[x][y] = temp[3]
        elif temp[0] == "UPDATE" and len(temp) == 3:
            for i, r in enumerate(value):
                for j, c in enumerate(r):
                    if c == temp[1]:
                        value[i][j] = temp[2]
        elif temp[0] == "MERGE":
            union_parent(int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]))
        elif temp[0] == "UNMERGE":
            x, y = find_parent(int(temp[1]), int(temp[2]))
            val = value[x][y]
            temp_li = []
            # for i in range(51):
            #     for j in range(51):
            #         if find_parent(i, j) == [x, y]:
            #             print(i, j, find_parent(i, j), pyo[i][j])
            #             pyo[i][j] = [i, j]
            #             value[i][j] = "EMPTY"
            #         if i == 4 and j == 4:
            #             print(i, j, find_parent(i, j))
            # value[int(temp[1])][int(temp[2])] = val
            for i in range(51):
                for j in range(51):
                    if i == int(temp[1]) and j == int(temp[2]):
                        continue
                    if find_parent(i, j) == [x, y]:
                        temp_li.append([i, j])
            for x, y in temp_li:
                pyo[x][y] = [x, y]
                value[x][y] = "EMPTY"
            pyo[int(temp[1])][int(temp[2])] = [int(temp[1]), int(temp[2])]
            value[int(temp[1])][int(temp[2])] = val
        else:
            x, y = find_parent(int(temp[1]), int(temp[2]))
            answer.append(value[x][y])
        print(pyo[4][4], value[4][4])
    return answer

# 문제 접근 방법
# # 모든 값을 확인하면서 풀려고 했고 가능했는데
# # 멋이 없어서 union-find라는 알고리즘을 배워서 풀어봄
# 새로 배운 python
# # python은 아니지만 union-find 알고리즘
# # 재귀적으로 부모를 찾는 함수와 부모끼리 합치는 함수로 이루어진 알고리즘
# # set을 활용해서 해당 좌표를 넣어볼까 했는데 union-find가 더 쉽게 구현할 수 있었다.