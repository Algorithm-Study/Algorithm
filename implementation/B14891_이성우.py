from collections import deque
def sol(num: int, direction: int) -> None:
    visited[num] = 1
    
    if 0 < num-1 and visited[num-1] == 0 \
        and gears[num-1][2] != gears[num][-2]:
        sol(num-1, direction*(-1))
            
    if num+1 <= 4 and visited[num+1] == 0 \
        and gears[num+1][-2] != gears[num][2]:
        sol(num+1, direction*(-1))
        
    gears[num].rotate(direction)
    
gear0 = [0]*8
gear1 = deque(input())
gear2 = deque(input())
gear3 = deque(input())
gear4 = deque(input())
gears = [gear0, gear1, gear2, gear3, gear4]

n = int(input())
for _ in range(n):
    num, d = map(int, input().split())
    visited = [0]*5
    sol(num, d)

print(int(gear1[0]) + int(gear2[0])*2 + int(gear3[0])*4 + int(gear4[0])*8)