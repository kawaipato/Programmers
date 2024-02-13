def Divisor(num):
        wow = []
        for i in range(1,int(num**(1/2))+1):
            if num % i == 0:
                wow.append(i)
                wow.append(num//i)
        return len(set(wow))
def solution(number, limit, power):
    return sum([Divisor(num) if Divisor(num) <= limit else power for num in range(1,number+1) ])