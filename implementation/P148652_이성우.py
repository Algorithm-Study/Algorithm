def solution(n, l, r):
    def cantor(n,i):
        answer = 0

        while n > 0:
            if i//(5**(n-1)) == 2:
                answer += (4**(n-1))*2
                break
            for a in range((i//(5**(n-1)))):
                if a == 2:
                    continue
                answer += (4**(n-1))

            i = i%(5**(n-1))
            # print(i)
            n -= 1
        return answer
    
    return cantor(n,r) - cantor(n,l-1)