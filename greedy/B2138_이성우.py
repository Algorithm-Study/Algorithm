n = int(input())
prob = list(map(int, input()))
target = list(map(int, input()))

def on_off(a, b):
    tmp = a[:]
    cnt = 0
    for i in range(1, n):
        if tmp[i-1] == b[i-1]:
            continue
        
        cnt += 1
        for j in range(i-1, i+2):
            if j < n:
                tmp[j] = 1 - tmp[j]
    return cnt if tmp == b else 1e9

answer = on_off(prob, target)

prob[0] = int(not(prob[0]))
prob[1] = int(not(prob[1]))

answer = min(answer, on_off(prob, target) + 1)
print(answer if answer != 1e9 else -1)