def solution(record):
    answer = []
    print_msg = []
    nn_dict = {}
    for rec in record:
        ls = rec.split()
        if ls[0] == 'Enter':
            print_msg.append([ls[0], ls[1]])
            nn_dict[ls[1]] = ls[2]
        elif ls[0] == 'Leave':
            print_msg.append([ls[0], ls[1]])
        else:
            nn_dict[ls[1]] = ls[2]
    for msg in print_msg:
        if msg[0] == 'Enter':
            answer.append(f"{nn_dict[msg[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nn_dict[msg[1]]}님이 나갔습니다.")
    return answer

# 문제 접근 방법
# # 