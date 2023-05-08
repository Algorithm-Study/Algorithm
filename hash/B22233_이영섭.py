import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keyword = {}
for _ in range(N):
    keyword[input().rstrip()] = 1
writing = set()
for _ in range(M):
    tp = input().rstrip().split(',')
    for i in tp:
        if i in keyword:
            keyword.pop(i)
    print(len(keyword))
    
# 문제 접근 방법
# # N 10만, M 10만이므로 list말고 dict를 사용
# # sys.stdin.readlin 안써서 시간초과
# # rstrip 안써서 틀렸습니다