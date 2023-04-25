def solution(book_time):
    times = [0]*(1440)
    book_time_sort = []
    answer = 0
    tmp = 0
    for start_time, end_time in book_time:
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))
        start_total = start_hour*60 + start_minute
        end_total = end_hour*60 + end_minute
        book_time_sort.append([start_total, min(end_total+10, 1439)])

    for time in book_time_sort:
        times[time[0]] += 1
        times[time[1]] -= 1
        
    for i in range(len(times)):
        tmp += times[i]
        answer = max(answer, tmp)

    return answer