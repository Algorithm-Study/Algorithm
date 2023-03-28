
def solution(n):
    total = sum([x for x in range(1,n+1)])
    triangle = [[0]*x for x in range(1,n+1)]
    op = ['vertical', 'horizontal', 'diagonal']
    x, y= 0, 0
    curr = 1
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            if op[(n-i)%3] == 'vertical':
                triangle[x][y] = curr
                if j != 1:
                    x+=1
                curr +=1
            elif op[(n-i)%3] == 'horizontal':
                #print(x,y)
                y+=1
                triangle[x][y] = curr
                curr +=1
            else:
                #print(x,y)
                y-=1
                x-=1
                triangle[x][y] = curr
                curr +=1
                if j == 1:
                    x+=1
    answer = []
    for t in triangle:
        answer += t
    return answer
print(solution(4))