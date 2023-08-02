def solution(cacheSize, cities):
    L = []
    n = 0
    for city in cities:
        if len(L) == cacheSize:
            if L.count(city.lower()) > 0:
                L.remove(city.lower())
                L.append(city.lower())
                n += 1
            else:
                if len(L) != 0:
                    L.pop(0)
                    L.append(city.lower())
                n += 5
        else:
            if L.count(city.lower()) > 0:
                L.remove(city.lower())
                L.append(city.lower())
                n += 1
            else:
                L.append(city.lower())
                n += 5
    return n