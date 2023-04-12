def solution(scores):
    w = scores[0]
    scores.sort(key = lambda x: x[0] + x[1])
    mx, my = 0,0
    msum = 0
    mlist = []
    i = 1
    
    while scores:
        x, y = scores.pop()
        
        # 여기서 등호(=)를 넣으면 테케 24번, 25번 시간초과 뜸
        if mx < x or my < y:
            mlist.append([x,y])
            mx, my = max(mx, x), max(my, y)
        # 여기도 동일 (정렬에서 x[0] 기준 빼서 좀 널널해짐) 
        if x + y > msum:
            mlist.append([x,y])
            msum = x + y
            
        if w[0] + w[1] >= x + y:
            break
        elif w[0] < x and w[1] < y:
            return -1
        else:
            i += 1
            
        if w[0] + w[1] < x + y:
            for z in mlist:
                if x < z[0] and y < z[1]:
                    i -= 1
                    break
    return i