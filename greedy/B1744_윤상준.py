import bisect
n = int(input())
sequence = [int(input()) for _ in range(n)]
sequence.sort()
negative = sequence[:bisect.bisect_right(sequence, 0)]
one = sequence[bisect.bisect_right(sequence, 0):bisect.bisect_right(sequence, 1)]
positive = sequence[bisect.bisect_right(sequence, 1):]
positive.sort(reverse = True)
result = 0
pos_length, neg_length = len(positive), len(negative)
for i in range(0,pos_length-1,2):
    result += positive[i]*positive[i+1]
for i in range(0,neg_length-1,2):
    result += negative[i]*negative[i+1]
if pos_length % 2 == 1:
    result += positive[-1]
if neg_length % 2 == 1:
    result += negative[-1]
result += sum(one)
print(result)

# 1인 경우 묶어서 계산하면 손해
# 이외의 수의 경우 절대값이 큰 값끼리 곱해야 큰 값을 얻을 수 있음
# 0은 음수 제거 용도로 사용하는 게 best
# 0을 포함한 음수, 1만 속한 리스트, 1을 제외한 양수 리스트로 나누어서 계산하면 쉽게 해결 가능