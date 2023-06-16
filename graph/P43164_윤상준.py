def solution(tickets):
    used = [0] * len(tickets)
    answer = []
    visited = [0] * len(tickets)
    def dfs(start, course):
        if len(course) == len(tickets) + 1:
            answer.append(course)
            return
        for i in range(len(tickets)):
            if start == tickets[i][0] and visited[i] == 0:
                visited[i] = 1
                dfs(tickets[i][1], course+[tickets[i][1]])
                visited[i] = 0
    dfs('ICN', ['ICN'])
    answer.sort()
    return answer[0]
# dfs으로 순차적으로 방문하면 해결되는 문제(기본 유형)