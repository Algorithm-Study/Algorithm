def solution(tickets):
    answer=[]
    tmp = []

    def dfs(start, tickets, tmp):
        tmp.append(start)
        
        if len(tickets) == 1:
            tmp.append(tickets[0][1])
            answer.append(tmp)
        else:
            for t in tickets:
                if start == t[0]:
                    tickets_copy = tickets.copy()
                    tickets_copy.remove(t)
                    dfs(t[1],tickets_copy, tmp.copy())
                    
    dfs('ICN', tickets, tmp)
    return min(answer)