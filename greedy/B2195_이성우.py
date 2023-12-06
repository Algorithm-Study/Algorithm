s = input()
p = input()
answer = 0
start = 0
end = 0
while True:
    if start == len(p):
        break
    for i in range(len(s)-(end-start)):
        # 같은 문자가 있으면 한 글자 뒤까지 확인
        if p[start:end+1] == s[i:i+(end-start)+1]:
            end += 1
            break
    # 없으면 이전 인덱스로 와서 다시 시작
    else:
        answer += 1
        end -= 1
        start = end+1
        end = start
print(answer)