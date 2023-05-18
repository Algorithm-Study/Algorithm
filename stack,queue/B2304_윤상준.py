n = int(int(input()))
warehouse = [0]*1001
max_pillar = 0
max_index = 0
end_index = 0
for _ in range(n):
    pos, length = map(int, input().split())
    warehouse[pos] = length
    if max_pillar < length:
        max_pillar = length
        max_index = pos
    end_index = max(end_index, pos)
current = warehouse[0]
square = 0
for i in range(max_index+1):
    if current < warehouse[i]:
        current = warehouse[i]
    square += current
current = warehouse[end_index]
for i in range(end_index, max_index, -1):
    if current < warehouse[i]:
        current = warehouse[i]
    square += current
print(square)

# stack을 사용하지 않아도 문제 해결 가능
# 높이 위치 모두 1000이내이기 때문에 리스트를 미리 선언해서 구현 가능