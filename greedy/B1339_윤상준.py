n = int(input())
str2int = {}
for i in range(ord('A'), ord('Z')+1):
    str2int[chr(i)] = 0
data = []
for _ in range(n):
    word = input()
    word = '0'*(8-len(word)) + word
    data.append(word)
    
for i in range(8):
    for j in range(n):
        if data[j][i] != '0':
            str2int[data[j][i]] += 10**(7-i)
s_str2int = sorted(str2int.items(), key = lambda x: (-x[1]))
total = 0
val = 9
for i in range(9):
    total += s_str2int[i][1] * val
    val -= 1
print(total)
# 각 알파벳의 자릿수만큼 더 해 준 후 내림차순으로 정렬해서 순차적으로 9부터 곱해서 더하면 문제 해결 가능