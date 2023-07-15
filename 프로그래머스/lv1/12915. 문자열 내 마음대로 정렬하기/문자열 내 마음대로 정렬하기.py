from operator import itemgetter, attrgetter, methodcaller
def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))