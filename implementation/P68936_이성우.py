def solution(arr: list) -> list:
    answer = [0,0]

    def check(n: int, arr: list) -> None:
        # 더 이상 분할할 수 없으면 원소 값을 더해준다
        if n == 1:
            for i in range(n):
                for j in range(n):
                    answer[arr[i][j]] += 1
        else:
            # 배열 내의 원소 확인
            cnt_1 = 0
            cnt_0 = 0
            for i in range(n):
                for j in range(n):
                    if arr[i][j] == 1:
                        cnt_1 += 1
                    else:
                        cnt_0 += 1
                if cnt_1*cnt_0 != 0:
                    break
            # 배열의 모든 원소가 1이면 answer[1] += 1
            if cnt_1 == n*n:
                answer[1] += 1
            # 배열의 모든 원소가 0이면 answer[0] += 0
            elif cnt_0 == n*n:
                answer[0] += 1
            # 둘다 아니면 분할
            else:
                tmp = [i[0:n//2] for i in arr[0:n//2]]
                check(n//2, tmp)
                tmp = [i[n//2:n] for i in arr[0:n//2]]
                check(n//2, tmp)
                tmp = [i[0:n//2] for i in arr[n//2:n]]
                check(n//2, tmp)
                tmp = [i[n//2:n] for i in arr[n//2:n]]
                check(n//2, tmp)
                    
    check(len(arr), arr)
    return answer