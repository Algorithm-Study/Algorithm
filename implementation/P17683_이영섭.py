def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
    answer, max_len = '(None)', 0
    musicinfos_list = []
    akbo = []
    
    for music in musicinfos:
        
        temp = music.split(',')
        
        end_time = temp[1].split(":")
        start_time = temp[0].split(":")
        during_time = int(end_time[0]) * 60 + int(end_time[1]) - int(start_time[0]) * 60 - int(start_time[1])
        
        new_music = temp[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
        music_len = len(new_music)
        akbo_tp = new_music * (during_time // music_len) + new_music[:(during_time % music_len)]
        akbo.append((akbo_tp, during_time, temp[2]))
    
    for ab in akbo:
        if m in ab[0] and ab[1] > max_len:
            answer = ab[2]
            max_len = ab[1]
            
    return answer

# 문제 접근 방법
# # Counter를 사용하여 #의 개수를 빼준 뒤, 비교하려 했으나 in으로 비교하려면 맨 뒤에 #이 붙은 것과 안 붙은 것을 구분해야함
# # 따라서 replace를 사용해 #이 붙은 음계를 소문자로 치환하여 해결