n, k = map(int, input().split())
data = [0]*k+list(input()) + [0]*k
answer = 0
for i in range(k, n+k):
    print(data)
    if data[i] == 'H':
        for j in range(i-k,i+k+1):
            if data[j] == 'P':
                data[j] = 0
                answer += 1
                break
print(answer)    
