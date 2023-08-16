from collections import deque

N = int(input())
gear = []
for _ in range(N):
    gear.append(deque(map(int, input())))
    
K = int(input())
rotation = []
for _ in range(K):
    i, j = map(int, input().split())
    rotation.append([i-1, j])
            
for num, d in rotation:
    tmp = [(num, d)]
    
    left = num - 1
    dl = -d
    while left >= 0 and gear[left][2] != gear[left+1][-2]:
        tmp.append((left, dl))
        left -= 1
        dl = -dl

    right = num + 1
    dr = -d
    while right < N and gear[right-1][2] != gear[right][-2]:
        tmp.append((right, dr))
        right += 1
        dr = -dr

    for t, dt in tmp:
        gear[t].rotate(dt)
        
answer = 0
for g in gear:
    if g[0] == 1:
        answer += 1
print(answer)