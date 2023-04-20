# slicing의 시간복잡도 O(b-a) -> 해당 방식을 채택할 경우 시간 초과 발생;;
# replace의 시간복잡도 O(n^2)
# join의 시간복잡도 O(n)
#=========================최종 제출=========================
import sys
input = sys.stdin.readline
data = str(input().rstrip())
find = str(input().rstrip())
result = []
n = len(find)
for d in data:
    result.append(d)
    if len(result) >= n and find == ''.join(result[-n:]):
        del result[-n:]
            
if len(result) == 0:
    print('FRULA')
else:
    print(''.join(result))
#=========================최종 제출=========================

#=========================처음 구현=========================
# 47%에서 timeout
data = str(input())
find = str(input())
while find in data:
    tmp = list(data.split(find))
    data = ''
    for w in tmp:
        data += w 
if len(data) == 0:
    print('FRULA')
else:
    print(data)
#=========================다음 구현=========================
data = str(input())
find = str(input())
while find in data:
    tmp = list(data.split(find))
    data = ''.join(tmp)
if len(data) == 0:
    print('FRULA')
else:
    print(data)
#=========================다음 구현=========================
data = str(input())
find = str(input())
result = ''
n = len(find)
for d in data:
    result += d
    if find in result:
        result = result[:-n]    
if len(result) == 0:
    print('FRULA')
else:
    print(result)