def solution(dirs):
    move = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    answer = 0
    start = [0,0]
    record = []
    for dir in dirs:
        way = move[dir]
        end = [min(max(start[0] + way[0], -5), 5), min(max(start[1] + way[1], -5), 5)]
        if start + end not in record and end + start not in record and start != end:
            record.append(start+end)
            answer+= 1
        start = end
    return answer