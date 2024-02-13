def Divisor(num):
        wow = 0
        for i in range(1,int(num**(1/2))+1):
            if num % i == 0:
                wow += 1
                if (i**2) != num:
                    wow += 1
        return wow
def solution(number, limit, power):
    ans = 0
    for n in range(1,number+1):
        a = Divisor(n)
        if a > limit:
            ans += power
        else:
            ans += a
    return ans