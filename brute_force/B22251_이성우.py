n, k, p, x = map(int, input().split())

d = {'0':'1110111',
     '1':'0010010',
     '2':'1011101',
     '3':'1011011',
     '4':'0111010',
     '5':'1101011',
     '6':'1101111',
     '7':'1010010',
     '8':'1111111',
     '9':'1111011'}

prob = str(x).zfill(k)
answer = 0

for i in range(1, n+1):
    zfill_i = str(i).zfill(k)
    cnt = 0
    for a, b in zip(prob, zfill_i):
        for idx in range(7):
            if d[a][idx] != d[b][idx]:
                cnt += 1
        
    if cnt <= p:
        answer += 1
        
print(answer-1)