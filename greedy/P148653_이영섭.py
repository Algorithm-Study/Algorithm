def solution(storey):
    answer = 0
    while storey > 0:
        rem = storey % 10
        if 6 <= rem and rem <= 9:
            answer += 10 - rem
            storey += 10 - rem
        elif rem == 5 and (storey / 10) % 10 >= 5:
            answer += 10 - rem
            storey += 10 - rem
        else:
            answer += rem
        storey //= 10
    return answer

# 문제 접근 방법
# # 주어진 숫자들이 모두 배수 관계를 이루고 있으므로 greedy로 해결 가능
# # 0 x 1~5- 6~9+
# # 나머지가 5이고 그 윗 자리 값이 5 이상인 경우 100으로 만드는 것이 이득