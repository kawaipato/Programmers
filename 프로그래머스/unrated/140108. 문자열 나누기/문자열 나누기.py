def solution(s):
    ans, stack = 0, ["", 0, 0]
    for ss in s:
        if stack[0] == "":
            stack[0] = ss
            stack[1] += 1
        else:
            if stack[0] == ss:
                stack[1] += 1
            else:
                stack[2] += 1
            if stack[1] == stack[2]:
                ans += 1
                stack = ["", 0, 0]
        # print(stack)
    if stack != ["",0,0]:
        ans += 1
    return ans