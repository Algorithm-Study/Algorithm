def solution(commands):
    db = [['EMPTY']*51 for _ in range(51)]
    merge_db = [[None]*51 for _ in range(51)]
    answer = []
    for command in commands:
        command = list(map(str, command.split()))
        if command[0] == 'UPDATE' and len(command) == 4:
            db, merge_db = update_1(db, merge_db, int(command[1]), int(command[2]), command[3])
        elif command[0] == 'UPDATE' and len(command) == 3:
            db, merge_db = update_2(db, merge_db, command[1], command[2])
        elif command[0] == 'MERGE':
            db, merge_db = merge(db, merge_db, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == 'UNMERGE':
            db, merge_db = unmerge(db, merge_db, int(command[1]), int(command[2]))
        elif command[0] == 'PRINT':
            answer.append(db[int(command[1])][int(command[2])])
            
    return answer

def update_1(db, merge_db, r,c,value):
    db[r][c] = value
    if merge_db[r][c] != None:
        for x in merge_db[r][c]:
            r2, c2 = x
            db[r2][c2] = value
    return db, merge_db

def update_2(db, merge_db, value1, value2):
    for i in range(51):
        for j in range(51):
            if db[i][j] == value1:
                db[i][j] = value2
    return db, merge_db

def merge(db, merge_db, r1, c1, r2, c2):
    if merge_db[r1][c1] != None:
        merge_db[r1][c1].append([r2, c2])
    else:
        merge_db[r1][c1] = [[r2, c2]]
        
    if merge_db[r2][c2] != None:
        merge_db[r2][c2].append([r1, c1])
    else:
        merge_db[r2][c2] = [[r1, c1]]
        
    if db[r1][c1] != 'EMPTY':
        db[r2][c2] = db[r1][c1]
    else:
        db[r1][c1] = db[r2][c2]
    return db, merge_db

def unmerge(db, merge_db, r, c):
    if merge_db[r][c] != None:
        for x in merge_db[r][c]:
            r2, c2 = x
            db[r2][c2] = "EMPTY"
            merge_db[r2][c2] = None
        else:
            merge_db[r][c] = None
    return db, merge_db

command = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
print(solution(command))