def solution(plans):
    plans.sort(key = lambda x: x[1])

    answer = []
    stack = []

    for subject, start, time in plans:
        h, m = map(int, start.split(':'))
        start = 60*h+m
        time = int(time)

        if stack:
            prev_subject, prev_start, prev_time = stack.pop()
            extra_time = start - prev_start

            if extra_time < prev_time:
                stack.append((prev_subject, prev_start, prev_time-extra_time))
            else:
                answer.append(prev_subject)
                extra_time = extra_time - prev_time

                while stack and extra_time :
                    prev_subject, prev_start, prev_time = stack.pop()

                    if extra_time < prev_time:
                        stack.append((prev_subject, prev_start, prev_time-extra_time))
                        break
                    else:
                        answer.append(prev_subject)
                        extra_time = extra_time - prev_time

        stack.append((subject, start, time))

    answer.extend([s for s, _, _ in stack[::-1]])

    return answer