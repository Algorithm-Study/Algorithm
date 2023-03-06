#변경 다 추적한 다음에 결과 생성
def solution(record):
    id2name = {}
    op_list = []
    id_list = []
    answer = []
    for r in record:
        if r.startswith('Enter') or r.startswith('Change'):
            op, id, name = r.split()
        else:
            op, id = r.split()
        op_list.append(op)
        id_list.append(id)
        if op == 'Enter':
            id2name[id] = name
        elif op == 'Change':
            id2name[id] = name
    for idx, o in enumerate(op_list):
        notify = ''
        if o == "Enter":
            notify += id2name[id_list[idx]]
            notify += "님이 들어왔습니다."
            answer.append(notify)
        elif o == "Leave":
            notify += id2name[id_list[idx]]
            notify += "님이 나갔습니다."
            answer.append(notify)       
    return answer