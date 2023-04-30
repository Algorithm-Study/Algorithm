n = int(input())
ref_word = list(input())
answer = 0
for _ in range(n-1):
    tmp = ref_word[:]
    word = input()
    cnt = 0
    for w in word:
        if w in tmp:
            tmp.remove(w)
        else:
            cnt += 1
    
    if cnt < 2 and len(tmp) < 2:
        answer +=1
        
print(answer)