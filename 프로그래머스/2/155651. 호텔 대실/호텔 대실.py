from heapq import heappush, heappop
def solution(book_time):
    rooms, books, ans = [], [], 0
    for book in book_time:
        start, end = book
        s1, s2 = start.split(':')
        e1, e2 = end.split(':')
        st = int(s1) * 60 + int(s2)
        et = int(e1) * 60 + int(e2)
        heappush(books, [st,et])
    while books:
        st, et = heappop(books)
        if not rooms:
            rooms.append([et,st])
        else:
            room = heappop(rooms)
            if room[0] + 10 > st:
                heappush(rooms,room)
            heappush(rooms,[et,st])
    ans = len(rooms)
    return ans
