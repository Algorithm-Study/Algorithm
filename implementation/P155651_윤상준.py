def solution(book_time):
    book_time.sort(key=lambda x: (x[0], x[1]))
    answer = 1
    end_time = list(map(int,book_time[0][1].split(':')))
    room_list = [end_time[0]*60 + end_time[1] + 10]
    for book in book_time[1:]:
        start_time = list(map(int,book[0].split(':')))
        end_time = list(map(int,book[1].split(':')))
        time = start_time[0]*60+start_time[1]
        flag = 0
        for i in range(len(room_list)):
            if room_list[i] <= time:
                room_list[i] = end_time[0]*60+end_time[1] + 10
                flag = 1
                break
        if flag == 0:
            answer += 1
            room_list.append(end_time[0]*60+end_time[1] + 10)    
    return answer