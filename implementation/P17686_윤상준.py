def solution(files):
    sort_level = []
    for idx, file in enumerate(files):
        file = file.lower()
        flag = 0
        #head, number, idx 순 정렬 
        file_info = ['', '', idx]
        for f in file:
            if f.isdigit():
                flag = 1
                file_info[1]+= f
            else:
                if flag == 1:
                    break
                else:
                    file_info[0]+=f
        sort_level.append(file_info)
    sort_level.sort(key = lambda x: (x[0], int(x[1]), x[2]))
    answer = [files[x[2]] for x in sort_level]
    return answer