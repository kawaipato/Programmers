def solution(book_time):
    dic = [0 for _ in range(60*24)]
    for book in book_time:
        start = int(book[0][:2]) * 60 + int(book[0][3:])
        end = int(book[1][:2]) * 60 + int(book[1][3:]) + 10
        if end > 60*24 - 1:
            end = 60*24 - 1
        for i in range(start,end):
            dic[i] += 1
    return max(dic)
        