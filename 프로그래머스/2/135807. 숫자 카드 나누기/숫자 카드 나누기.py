def solution(arrayA, arrayB):
    def gcd(a,b):
        while b != 0:
            a, b = b, a%b
        return a
    gcdA, gcdB = arrayA[0], arrayB[0]
    for a, b in zip(arrayA, arrayB):
        gcdA = gcd(gcdA,a)
        gcdB = gcd(gcdB,b)
    AA = sum([True for b in arrayB if b % gcdA != 0])
    BB = sum([True for a in arrayA if a % gcdB != 0])
    if len(arrayA) == AA or len(arrayB) == BB:
        return max(gcdA,gcdB)
    else: return 0