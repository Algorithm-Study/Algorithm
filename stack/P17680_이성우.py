from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    # cache = collections.deque(maxlen=cacheSize) 으로 size 제한 가능
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.append(city)
                cache.popleft()
            answer += 5

    return answer