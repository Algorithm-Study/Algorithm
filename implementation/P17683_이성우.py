def solution(m, musicinfos):
    music_infos = []
    answer = [[-1,0,'(None)']]
    new_m = ''
    n = 0
    
    for idx in range(len(m)):
        if m[idx] == '#':
            continue
        elif idx != len(m)-1 and m[idx+1] == '#':
            new_m += m[idx].lower()
        else:
            new_m += m[idx]
            
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        s_h, s_m = start.split(':')
        e_h, e_m = end.split(':')
        minutes = (int(e_h) - int(s_h))*60 + int(e_m) - int(s_m)
        new_melody = ''
        for idx in range(len(melody)):
            if melody[idx] == '#':
                continue
            elif idx != len(melody)-1 and melody[idx+1] == '#':
                new_melody += melody[idx].lower()
            else:
                new_melody += melody[idx]

        if new_m in (new_melody*(int(minutes//len(new_melody))+1))[:minutes]:
            answer.append([minutes,n,title])
            n += 1
            
    answer.sort(key = lambda x : [x[0], -x[1]])
    return answer[-1][2]