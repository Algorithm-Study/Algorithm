n = int(input())
dictionary = [(input(),x) for x in range(n)]
s_dictionary = sorted(dictionary)
max_info = [0]*n
for i in range(n-1):
    cnt = 0
    a, b = s_dictionary[i][0], s_dictionary[i+1][0]
    for j in range(min(len(a),len(b))):
        if a[j] == b[j]:
            cnt += 1
        else:
            break
    max_info[s_dictionary[i][1]] = max(max_info[s_dictionary[i][1]], cnt)
    max_info[s_dictionary[i+1][1]] = max(max_info[s_dictionary[i+1][1]], cnt)
max_start, prefix = max(max_info), ''
cnt = 0
for i in range(n):
    if cnt == 0:
        if max_info[i] == max_start:
            print(dictionary[i][0])
            cnt += 1
            prefix = dictionary[i][0][:max_start]
    else:
        if max_info[i] == max_start and dictionary[i][0][:max_start] == prefix:
            print(dictionary[i][0])
            break
# 정렬 이후 인접한 단어에 대해서 접두사 체크
# 이후 가장 빠른 단어를 선택
# 다음으로 접두사가 같은 단어 찾기
