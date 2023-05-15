n = int(input())
table = [0]*1_000_002
for _ in range(n):
    start, end = map(int, input().split())
    table[start] += 1
    table[end+1] -= 1
for i in range(1, 1_000_001):
    table[i] += table[i-1]
q = int(input())
when = list(map(int, input().split()))
for wh in when:
    print(table[wh])

# 누적 합 문제를 쉽게 풀 수 있는 imos 법을 활용하면 쉽게 풀이 가능
# imos 법: 문제의 시작 시간과 끝 시각에 대한 정보만 저장
# 첫 인덱스 부터 누적합을 계산