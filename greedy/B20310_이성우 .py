# 초기 변수 설정
n = list(input())
cnt_zero = n.count('0')//2
cnt_one = n.count('1')//2

# 앞에서부터 1을 제거
for num in n:
    if cnt_one and num == '1':
        n.remove('1')
        cnt_one -= 1

# 뒤에서부터 0을 제거하기 위해 뒤집어서 제거
n = n[::-1]

for num in n:
    if cnt_zero and num == '0':
        n.remove('0')
        cnt_zero -= 1

# 결과 반환
print(''.join(n[::-1]))