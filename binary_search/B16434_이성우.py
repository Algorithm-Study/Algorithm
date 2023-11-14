n, attack = map(int, input().split())
arr = []
for _ in range(n):
    t, a, h = map(int, input().split())
    arr.append((t, a, h))

def check(cur_atk, max_hp):
    cur_hp = max_hp
    
    # 던전 탐색
    for t, a, h in arr:
        
        # 전투시
        if t == 1:
            if h % cur_atk:
                cnt = h // cur_atk + 1
            else:
                cnt = h // cur_atk
            cur_hp -= a * (cnt-1)
            
        # 회복시
        else:
            cur_atk += a
            cur_hp = min(cur_hp+h, max_hp)
            
        # 사망시
        if cur_hp <= 0:
            return False
    return True

answer = 0
start, end = 1, n*(10**6)*(10**6)
while start <= end:
    mid = (start+end) // 2
    if check(attack, mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
        
print(answer)