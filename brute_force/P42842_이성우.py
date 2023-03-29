def solution(brown, yellow):
    for i in range(1, brown):
        
        # 테두리가 갈색 1줄로 칠해져 있기 때문에
        # 노란색과 갈색이 정해진 수로 맞는지 확인하고 반환
        if (2*yellow)/i+(2*i)+4 == brown:
            return [(brown+yellow)/(i+2) , i+2]