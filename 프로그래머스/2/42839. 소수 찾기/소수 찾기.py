from itertools import permutations
def solution(numbers):
    def is_prime(num):
        for n in range(2,int(num**0.5) + 1):
            if num % n == 0:
                return False
        return True
    lst, ans = [], 0
    for i in range(1,len(numbers)+1):
        lst += [int(''.join(n)) for n in permutations(numbers,i)]
    lst = list(set(lst))
    for t in lst:
        if is_prime(t) and t > 1:
            ans += 1
    return ans