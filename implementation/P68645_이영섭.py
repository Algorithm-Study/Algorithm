def triangle(answer, n, start, depth, bottom):
    if n <= 0: return
    val = start
    for idx, i in enumerate(range(n, n-2, -1)):
        now = idx % 3
        for j in range(i):
            temp = val + j
            if now == 0:
                answer[depth*2+j].append(temp) #0 6 2 3 4 
            elif now == 1:
                answer[bottom].append(temp)
        val += i
    val += n-2
    triangle(answer, n-3, val, depth+1, bottom-1)
    val -= n-2
    for j in range(n-2):
        temp = val + j
        answer[bottom-1-j].append(temp) #2 n-2 5 n-3
    return

def solution(n):
    answer = [[] for _ in range(n)]
    val = 1
    triangle(answer, n, val, 0, n-1)
    ans = [ans_val for i in answer for ans_val in i]
    return ans

# 문제 접근 방법
# # 재귀로 삼각형의 왼쪽변과 아랫변을 그리고 빠져나오면서 오른쪽 변 그리기