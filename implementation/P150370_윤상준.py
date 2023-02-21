def solution(today, terms, privacies):
    answer = []
    term = {} 
    year, month, date = list(map(int,today.split('.'))) 
    total_today = year*12*28 + month*28 + date
    
    for t in terms:
        term[t[0]] = int(t[2:])*28

    for i,p in enumerate(privacies):
        y,m,d = p.split('.')
        d,t = d.split()
        p = int(y)*12*28 + int(m)*28 + int(d)
        if p+term[t] <= total_today:
            answer.append(i+1)                 
    return answer