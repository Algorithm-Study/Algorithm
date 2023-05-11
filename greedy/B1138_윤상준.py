n = int(input())
info = list(map(int, input().split()))
line = [0]*n
for i in range(n):
    count = 0
    for j in range(n):
        if count == info[i] and line[j] == 0:
            line[j] = i + 1
            break
        elif line[j] == 0:
            count += 1

print(*line)
# 입력 순서대로 키 큰 사람 수만큼 0을 카운트
# 그 다음 0에 해당 사람 배치