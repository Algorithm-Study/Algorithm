def solution(files):
    answer = []
    all_files = []
    for idx, file in enumerate(files):
        isdigit = False
        ischar = False
        ftemp = []
        temp = ''
        for i, ch in enumerate(file):
            if ischar == False:
                if isdigit == ch.isdigit():
                    temp += ch
                elif isdigit == False and ch.isdigit():
                    ftemp.append(temp)
                    temp = ch
                    isdigit = True
                elif isdigit == True and not ch.isdigit():
                    ftemp.append(temp)
                    temp = ch
                    ischar = True
            else:
                temp += ch
                
            if i == len(file) - 1:
                if ischar == False:
                    ftemp.append(temp)
                    ftemp.append('')
                else:
                    ftemp.append(temp)
                ftemp.append(idx)
        all_files.append(ftemp)
    all_files = sorted(all_files, key = lambda x : (x[0].lower(), int(x[1]), x[3]))
    for af in all_files:
        answer.append(''.join(af[:3]))
    return answer

# 문제 접근 방식
# # python은 sorted 함수를 이용하여 정렬할 key 값을 선정할 수 있으므로
# # file을 HEAD, NUMBER, TAIL로 나눠서 저장하고 이를 정렬