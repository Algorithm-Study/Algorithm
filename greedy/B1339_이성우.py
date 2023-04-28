n = int(input())
words = []
alpha_val = {}
for _ in range(n):
    words.append(input())
    
for word in words:
    for idx in range(len(word)):
        if word[idx] not in alpha_val:
            alpha_val[word[idx]] = 10**(len(word)-1-idx)
        else:
            alpha_val[word[idx]] += 10**(len(word)-1-idx)

            
alpha_val = sorted(alpha_val.items(), key=lambda x: x[1], reverse=True)

alpha_to_num = {}

num = 9
for alpha in alpha_val:
    alpha_to_num[alpha[0]] = num
    num -= 1
    
answer = 0
for word in words:
    num = ""
    for alpha in word:
        num += str(alpha_to_num[alpha])
        
    answer += int(num)

print(answer)