N = int(input())
sugang = []
for _ in range(N):
    si, ti = map(int, input().split())
    sugang.append((si, 1))
    sugang.append((ti, 0))
sugang.sort()
answer = 0
cnt = 0
for sg in sugang:
    if sg[1] == 1:
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt -= 1
print(answer)