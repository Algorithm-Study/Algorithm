change = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
def solution(m, musicinfos):
    for ch in change:
        m = m.replace(ch,change[ch])
    titles = []
    rhymes = []
    for idx, music in enumerate(musicinfos):
        start,end,title,rhyme = music.split(',')
        played = (int(end[:2]) - int(start[:2]))*60 + int(end[3:]) - int(start[3:])
        for ch in change:
            rhyme = rhyme.replace(ch, change[ch])
        length = len(rhyme)
        if played > length:
            rhymes.append([idx, rhyme * (played//length) + rhyme[:played % length]])
        else:
            rhymes.append([idx, rhyme[:played]])
        titles.append(title)
    rhymes.sort(key = lambda x: (-len(x[1]), x[0]))
    print(rhymes)
    for q,rhyme in rhymes:
        if m in rhyme:
            return titles[q]
    
    return "(None)"
# #이 들어가는 음이 있기 때문에 원할하게 진행하기 위해서는 이를 변환해야 함
# 변환 방법: maketrans, re, replace 등이 있음