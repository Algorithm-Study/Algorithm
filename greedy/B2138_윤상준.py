change = {'1': '0', '0':'1'}
n = int(input())
answer = list(input())
current = list(input())
current2 = [change[x] for x in current[:2]] + current[2:]
click1, click2 = 0, 1
for i in range(1,n):
    if current == answer:
        print(click1)
        exit()
    elif current2 == answer:
        print(click2)
        exit()
    if current[i-1] != answer[i-1]:
        click1 += 1
        current[i-1] = change[current[i-1]]
        current[i] = change[current[i]]
        if i != n-1:
            current[i+1] = change[current[i+1]]
    if current2[i-1] != answer[i-1]:
        click2 += 1
        current2[i-1] = change[current2[i-1]]
        current2[i] = change[current2[i]]
        if i != n-1:
            current2[i+1] = change[current2[i+1]]
if current == answer:
    print(click1)
elif current2 == answer:
    print(click2)
else:
    print(-1)
# 선택지를 제한하는 방식으로 진행
# 1번 스위치를 누르는 경우 or 누르지 않는 경우로 나눠서 진행