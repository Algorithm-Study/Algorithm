n = int(input())
value = list(map(int, input().split()))
min_values = sorted([min(value[0],value[5]), min(value[1],value[4]), min(value[2],value[3])])
one, two, three = min_values[0], sum(min_values[0:2]), sum(min_values)
total = one *(5*(n**2)-16*n +12) + two*(8*n -12) + three*4
if n  == 1:
    print(sum(sorted(value)[0:5]))
else:
    print(total)
# 주사위의 관계를 고려하여 최솟값 계산
# 1인 경우를 제외하고는 규칙이 존재(최대 3면까지 노출)
# 3면 노출 : 4개
# 2면 노출 : 4(n-2) + 4(n-1) -> 윗면 + 옆면
# 1면 노출 : (n-2)(n-2) + 4(n-2)(n-1) -> 윗면 + 옆면