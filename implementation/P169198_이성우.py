def solution(m, n, x, y, balls):
    answer = []
    for c in balls:
        val = []
        a, b = c[0], c[1]
        if x == a:
            if y > b:
                val.append((n-y + n-b)**2)
            else:
                val.append((y+b)**2)
            val.append((-x+m+m-a)**2+(y-b)**2)
            val.append((x+a)**2 + (y-b)**2)
        elif y == b:
            if x < a:
                val.append((x + a)**2)
            else:
                val.append((m-x + m-a)**2)
            val.append((a-x)**2+(-y+n+n-b)**2)
            val.append((a-x)**2+(y+b)**2)
        else:
            val.append( (x+a)**2+(y-b)**2)
            val.append( (-x+m+m-a)**2+(y-b)**2)
            val.append( (a-x)**2+(n+n-b-y)**2)
            val.append( (a-x)**2+(y+b)**2)
            # print(val)
        answer.append(min(val))
                
    return answer