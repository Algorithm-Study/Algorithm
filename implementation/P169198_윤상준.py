def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        temp = []
        #x-axis flip
        if ball[1] < startY or ball[0] != startX:
            new_ball = [ball[0], 2*n-ball[1]]
            temp.append((startX- new_ball[0])**2 + (startY - new_ball[1])**2)
        if ball[1] > startY or ball[0] != startX:
            new_ball = [ball[0], -ball[1]]
            temp.append((startX- new_ball[0])**2 + (startY - new_ball[1])**2)
        #y-axis flip
        if ball[0] < startX or ball[1] != startY:
            new_ball = [2*m-ball[0], ball[1]]
            temp.append((startX- new_ball[0])**2 + (startY - new_ball[1])**2)
        if ball[0] > startX or ball[1] != startY:
            new_ball = [-ball[0], ball[1]]
            temp.append((startX- new_ball[0])**2 + (startY - new_ball[1])**2)
        answer.append(min(temp))
    return answer