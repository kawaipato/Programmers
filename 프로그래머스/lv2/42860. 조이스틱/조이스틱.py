def solution(name):
    if set(name) == {'A'}:
        return 0
    ans, a,z = 987654321, ord('A'), ord('Z')
    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i]
        r_l = name[i::-1] + name[i+1:][::-1]
        for n in [l_r,r_l]:
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c) - a, (z + 1 - ord(c))) for c in n]
            ans = min(ans,i + sum(cnt) + len(cnt) - 1)
    return ans
    # for idx, n in enumerate(name):
    #     n = ord(n)
    #     if n == a:
    #         ans += 1
    #         A_stack.append(idx)
    #     else:
    #         ans += min(n - a, 26 - n + a) + 1
    # return A_stack