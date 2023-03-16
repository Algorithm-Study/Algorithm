def find(r: int, c: int) -> list:
    if parent[r][c] != (r, c):
        nr, nc = parent[r][c]
        parent[r][c] = find(nr, nc)
    return parent[r][c]


def update1(r: int, c: int, v: str) -> None:
    root = find(r, c)

    for i in range(n):
        for j in range(n):
            if find(i, j) == root:
                table[i][j] = v


def update2(v1: str, v2: str) -> None:
    for i in range(n):
        for j in range(n):
            r, c = find(i, j)

            if table[r][c] == v1:
                table[r][c] = v2


def merge(r1: int, c1: int, r2: int, c2: int) -> None:
    r1 ,c1 = find(r1, c1)
    r2 ,c2 = find(r2, c2)

    if [r1 ,c1] == [r2 ,c2]: return

    parent[r2][c2] = (r1, c1)
    v = table[r1][c1] if table[r1][c1] else table[r2][c2]
    update1(r1, c1, v)


def unmerge(r: int, c: int) -> None:
    root = find(r, c)
    v = table[root[0]][root[1]]

    mrg = [(i, j) for i in range(n) for j in range(n) if find(i, j) == root]

    for rt in mrg:
        r1, c1 = rt
        parent[r1][c1] = (r1, c1)

        if (r1, c1) != (r, c):
            table[r1][c1] = 0

    table[r][c] = v


def printer(r: int, c: int) -> None:
    r1, c1 = find(r, c)
    v = table[r1][c1]
    ans.append('EMPTY' if not v else v)


def solution(commands):

    global n
    global ans
    global table
    global parent

    n = 51
    ans = []
    table = [[0] * n for _ in range(n)]
    parent= [[(r, c) for c in range(n)] for r in range(n)]

    for command in commands:
        command = command.split()
        cmd, value = command[0], command[1:]

        if cmd == 'UPDATE':
            if len(value) == 3:
                r, c, v = value
                update1(int(r), int(c), v)

            else:
                v1, v2 = value
                update2(v1, v2)

        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, value)
            merge(r1, c1, r2, c2)

        elif cmd == 'UNMERGE':
            r, c = map(int, value)
            unmerge(r, c)

        else:
            r, c = map(int, value)
            printer(r, c)

    return ans
# def solution(commands):
#     db = [['EMPTY']*51 for _ in range(51)]
#     merge_db = [[None]*51 for _ in range(51)]
#     answer = []
#     for command in commands:
#         command = list(map(str, command.split()))
        
#         if command[0] == 'UPDATE' and len(command) == 4:
#             db, merge_db = update_1(db, merge_db, int(command[1]), int(command[2]), command[3])

#         elif command[0] == 'UPDATE' and len(command) == 3:
#             db, merge_db = update_2(db, merge_db, command[1], command[2])

#         elif command[0] == 'MERGE':
            
#             db, merge_db = merge(db, merge_db, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
            
#         elif command[0] == 'UNMERGE':
#             db, merge_db = unmerge(db, merge_db, int(command[1]), int(command[2]))
        
#         elif command[0] == 'PRINT':
#             answer.append(db[int(command[1])][int(command[2])])

#     return answer

# def update_1(db, merge_db, r,c,value):
#     db[r][c] = value
#     if merge_db[r][c] != None:
#         for x in merge_db[r][c]:
#             r2, c2 = x
#             db[r2][c2] = value
#     return db, merge_db

# def update_2(db, merge_db, value1, value2):
#     for i in range(51):
#         for j in range(51):
#             if db[i][j] == value1:
#                 db[i][j] = value2
#     return db, merge_db

# def merge(db, merge_db, r1, c1, r2, c2):
#     change_r1c1 = False
#     change_r2c2 = False
#     if merge_db[r1][c1] != None:
#         for a in merge_db[r1][c1]:
#             a1, a2 = a
#             merge_db[a1][a2].append([r2,c2])
#         merge_db[r1][c1].append([r2, c2])
#     else:
#         change_r1c1 = True

#     if merge_db[r2][c2] != None:
#         for b in merge_db[r2][c2]:
#             b1, b2 = b
#             merge_db[a1][a2].append([r1,c1])
#         merge_db[r2][c2].append([r1, c1])
#     else:
#         change_r2c2 = True
        
#     if change_r1c1:
#         merge_db[r1][c1] = [[r2, c2]]
#     if change_r2c2:
#         merge_db[r2][c2] = [[r1, c1]]
        
#     if db[r1][c1] != 'EMPTY' and db[r2][c2] != 'EMPTY':
#         db[r2][c2] = db[r1][c1]
#     elif db[r1][c1] == 'EMPTY' and db[r2][c2] != 'EMPTY':
#         db[r1][c1] = db[r2][c2]
#     elif db[r1][c1] != 'EMPTY' and db[r2][c2] == 'EMPTY':
#         db[r2][c2] = db[r1][c1]
#     return db, merge_db

# def unmerge(db, merge_db, r, c):
#     if merge_db[r][c] != None:
#         for x in merge_db[r][c]:
#             r2, c2 = x
#             db[r2][c2] = "EMPTY"
#             merge_db[r2][c2] = None
#         else:
#             merge_db[r][c] = None
#     return db, merge_db