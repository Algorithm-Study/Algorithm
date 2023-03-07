def solution(records):
    answers = []
    uid_nick = {}
    for record in records:
        log = record.split()
        if log[0] == 'Enter':
            answers.append([log[1], log[0]])
            uid_nick[log[1]] = log[2]
        elif log[0] == 'Leave':
            answers.append([log[1], log[0]])
        else:
            uid_nick[log[1]] = log[2]
            
    for i, answer in enumerate(answers):
        if answer[1] == 'Enter':
            answers[i] = f'{uid_nick[answer[0]]}님이 들어왔습니다.'
        else:
            answers[i] = f'{uid_nick[answer[0]]}님이 나갔습니다.'

    return answers