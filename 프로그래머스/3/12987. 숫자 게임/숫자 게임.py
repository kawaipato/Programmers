def solution(A, B):
    ans = 0
    A.sort();   B.sort()
    while B:
        if A[0] < B[0]:
            A.pop(0);   B.pop(0);
            ans += 1
        else:
            B.pop(0)
    return ans