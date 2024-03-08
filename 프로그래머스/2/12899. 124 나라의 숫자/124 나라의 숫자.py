def solution(n):
    new_n = ''
    while n:
        imsi = n % 3
        if not imsi:
            imsi = 3
            n -= 1
        new_n += str(imsi)
        n //= 3
    new_n = new_n.replace('3','4')
    return new_n[::-1]