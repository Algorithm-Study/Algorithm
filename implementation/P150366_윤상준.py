#가리키기 posrc
def solution(commands):
    answer = []
    cells = [ [['EMPTY'] for _ in range(51)] for _ in range(51)]
    #print(cells[0][0][0])
    for cmd_line in commands:
        cmd = cmd_line.split()
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                if cells[int(cmd[1])][int(cmd[2])][0].startswith('pos'):
                    r,c = cells[int(cmd[1])][int(cmd[2])][0][-2], cells[int(cmd[1])][int(cmd[2])][0][-1]
                    cells[int(r)][int(c)][0] = cmd[3] 
                else:
                    cells[int(cmd[1])][int(cmd[2])][0] = cmd[3]
            else:
                for i in range(1,51):
                    for j in range(1,51):
                        if cells[i][j][0] == cmd[1]:
                            cells[i][j][0] = cmd[2]
        elif cmd[0] == 'MERGE':
            if cmd[1] == cmd[3] and cmd[2] == cmd[4]:
                break
            else:
                if cells[int(cmd[1])][int(cmd[2])][0] != 'EMPTY' and not cells[int(cmd[1])][int(cmd[2])][0].startswith('pos'):
                    cells[int(cmd[3])][int(cmd[4])][0] = 'pos'+cmd[1] + cmd[2]
                elif cells[int(cmd[1])][int(cmd[2])][0] != 'EMPTY' and cells[int(cmd[1])][int(cmd[2])][0].startswith('pos'):
                    if cells[int(cmd[3])][int(cmd[4])][0].startswith('pos'):
                        r,c =  cells[int(cmd[3])][int(cmd[4])][0][-2],  cells[int(cmd[3])][int(cmd[4])][0][-1]
                        for i in range(1,51):
                            for j in range(1,51):
                                if cells[i][j][0] == 'pos'+r+c:
                                    cells[i][j][0] = cells[int(cmd[1])][int(cmd[2])][0]
                    cells[int(cmd[3])][int(cmd[4])][0] = cells[int(cmd[1])][int(cmd[2])][0]
                elif cells[int(cmd[1])][int(cmd[2])][0] == 'EMPTY' and cells[int(cmd[3])][int(cmd[4])][0].startswith('pos'):
                    r,c =  cells[int(cmd[3])][int(cmd[4])][0][-2],  cells[int(cmd[3])][int(cmd[4])][0][-1]
                    cells[int(cmd[1])][int(cmd[2])][0] = cells[int(r)][int(c)][0]
                    cells[int(r)][int(c)][0] = 'pos'+cmd[1] + cmd[2]
                    for i in range(1,51):
                        for j in range(1,51):
                            if cells[i][j][0] == 'pos'+r+c:
                                cells[i][j][0] = 'pos'+cmd[1] + cmd[2]
                else:
                    cells[int(cmd[1])][int(cmd[2])][0] = cells[int(cmd[3])][int(cmd[4])][0]
                    cells[int(cmd[3])][int(cmd[4])][0] = 'pos'+cmd[1] + cmd[2]
                for i in range(1,51):
                    for j in range(1,51):
                        if cells[i][j][0] == 'pos'+cmd[3]+cmd[4]:
                            cells[i][j][0] = cells[int(cmd[3])][int(cmd[4])][0]
        elif cmd[0] == 'UNMERGE':
            if cells[int(cmd[1])][int(cmd[2])][0].startswith('pos'):
                r, c = cells[int(cmd[1])][int(cmd[2])][0][-2], cells[int(cmd[1])][int(cmd[2])][0][-1]
                cells[int(cmd[1])][int(cmd[2])][0] = cells[int(r)][int(c)][0]
                cells[int(r)][int(c)][0] = 'EMPTY'
            else:
                r, c = cmd[1], cmd[2]
            for i in range(1,51):
                    for j in range(1,51):
                        if cells[i][j][0] == 'pos'+r+c:
                            cells[i][j][0] = 'EMPTY'
        elif cmd[0] == 'PRINT':
            if cells[int(cmd[1])][int(cmd[2])][0].startswith('pos'):
                r, c = cells[int(cmd[1])][int(cmd[2])][0][-2], cells[int(cmd[1])][int(cmd[2])][0][-1]
                answer.append(cells[int(r)][int(c)][0])
            else:
                answer.append(cells[int(cmd[1])][int(cmd[2])][0])
        print("="*10)
        print(cells[1][1], cells[1][2], cells[1][3], cells[1][4])
        print(cells[2][1], cells[2][2], cells[2][3], cells[2][4])
        print(cells[3][1], cells[3][2], cells[3][3], cells[3][4])
        print(cells[4][1], cells[4][2], cells[4][3], cells[4][4])
    return answer

#=============================== 새 풀이 ==============================
values = ['EMPTY' for _ in range(51*51)]
parent = [i for i in range(51*51)]
def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(x ,y):
    root1 = find(x)
    root2 = find(y)
    if values[root1] == 'EMPTY' and values[root2] != 'EMPTY':
        parent[root1] = root2
        values[root1] = values[root2]
    else:
        parent[root2] = root1
        values[root2] = values[root1]

def solution(commands):
    answer = []
    for cmd_line in commands:
        cmd = cmd_line.split()
        if cmd[0]== "UPDATE":
            if len(cmd) == 4:
                root = find(50*int(cmd[1]) + int(cmd[2]))
                values[root] = cmd[3]
            else:
                for i in range(51,51*51):
                    if values[i] == cmd[1]:
                        values[i] = cmd[2]
        elif cmd[0] == "MERGE":
            x= 50*int(cmd[1]) + int(cmd[2])
            y= 50*int(cmd[3]) + int(cmd[4])
            if parent[x] != parent[y]:
                union(x,y)
        elif cmd[0] == "UNMERGE":
            root = find(50*int(cmd[1]) + int(cmd[2]))
            val = values[root]
            children = []
            for i in range(51,51*51):
                if find(i) == root:
                    children.append(i)
            for child in children:
                values[child] = "EMPTY"
                parent[child] = child
            values[50*int(cmd[1]) + int(cmd[2])] = val
        else:
            pos = find(50*int(cmd[1])+int(cmd[2]))
            answer.append(values[pos])
        for i in range(1,5):
            print(values[50*i+1: 50*i+5])
        print('='*20)
    
    return answer