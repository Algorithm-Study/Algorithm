n = int(input())
m = int(input())
sequence = input()
count, idx = 0, 0
temp  = 0
while idx < m-1:
    if sequence[idx:idx+3] == 'IOI':
        idx += 2
        temp += 1
        if temp == n:
            count += 1
            temp -= 1
    else:
        idx += 1
        temp = 0
print(count)

# 슬라이싱에 따른 시간초과로 인해 부분점수가 존재하는 문제

n = int(input())
m = int(input())
sequence = input()
ioi = ''.join(['I' if x%2 == 0 else 'O' for x in range(2*n+1)])
count = 0
for i in range(m-(2*n+1)+1):
    if sequence[i:].startswith(ioi):
        count += 1
print(count)

# 하나씩 증가시키면서 slicing 진행할 경우 시간초과로 인해 부분 점수를 받음
# 반복되는 IOI를 고려하여 인덱스 값을 변화시키면 제약 시간 안에 문제 풀이 가능