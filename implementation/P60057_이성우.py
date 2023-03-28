def solution(s):
    # answer 최대값으로 초기화
    answer = 1000
    
    # s 길이 1이면 1 반환
    if len(s) == 1:
        return 1
    
    # 압축 단위 i 설정 및 변수 초기화
    for i in range(1,len(s)//2+1):
        changed_s = ''
        cnt = 1
        tmp=s[:i]

        # s에서 잘라낼 j 범위 설정
        for j in range(i, len(s), i):
            
            # 잘라낸 단위가 앞 단어와 같다면 cnt +1
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                
                # cnt가 2이상이면 압축 후에 숫자를 붙이고 1이면 숫자를 붙이지 않고 그냥 붙인다
                if cnt!=1:
                    changed_s = changed_s + str(cnt)+tmp
                else:
                    changed_s = changed_s + tmp
                    
                # 비교할 단어 변경 후 cnt 초기화
                tmp=s[j:i+j]
                cnt = 1
                
        # 마지막 단어 처리
        if cnt!=1:
            changed_s = changed_s + str(cnt) + tmp
        else:
            changed_s = changed_s + tmp
            
        # 최소 값과 비교하여 최소값 갱신
        answer = min(len(changed_s), answer)
    return answer