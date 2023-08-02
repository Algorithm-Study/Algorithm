from itertools import combinations
import copy

def move_down():
    for i in range(n)[::-1]:
        if i == 0:
            arr[i] = [0]*m
        else:
            arr[i] = arr[i-1]
            
            
def kill_target(targets, cnt):
    for t in targets:
        arr[t[0]][t[1]] = 0
        
    cnt += len(targets)        
    return cnt
        
        
def target_search(case):
    targets = set()
    tmp = None
    
    for b in case:
        x, y = n, b
        dis = d + 1
        for j in range(m):
            for i in range(n):
                if arr[i][j] == 1 and abs(x-i) + abs(y-j) < dis:
                    dis = abs(x-i) + abs(y-j)
                    tmp = i, j
                        
        if tmp != None:
            targets.add(tmp)      

    return targets


def check_end():
    for i in range(n):
        if any(arr[i]):
            return True
            
    return False


n, m, d = map(int, input().split())
tmp_arr = [list(map(int, input().split())) for _ in range(n)]     
answer = 0
for case in combinations(range(m), 3):
    arr = copy.deepcopy(tmp_arr)
    cnt = 0
    while check_end():
        targets = target_search(case)
        cnt = kill_target(targets, cnt)
        move_down()
    answer = max(answer, cnt)
    
print(answer)