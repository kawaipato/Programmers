def cal(n1,n2,op):
    if op == "*":
        return n1 * n2
    elif op == '+':
        return n1 + n2
    return n1 - n2

from itertools import permutations
def solution(expression):
    answer, tool = 0, '*+-'
    c = list(permutations(tool,3))
    sik = expression
    for t in tool:  sik = sik.replace(t,' ')
    nums = [int(i) for i in sik.split(' ')]
    ops = [i for i in expression if not i.isdecimal()]
    
    for cc in c:    # Priority
        n_nums = nums
        n_ops = ops
        
        for ccc in cc:  # operater
            num_stack, op_stack = [], []
            num_stack.append(n_nums[0])
            for i in range(len(n_ops)): # operand
                num_stack.append(n_nums[i+1])
                op_stack.append(n_ops[i])
                
                if op_stack[-1] == ccc:
                    num1 = num_stack.pop(-1)
                    num2 = num_stack.pop(-1)
                    opp = op_stack.pop(-1)
                    num_stack.append(cal(num2,num1,opp))
            n_nums = num_stack
            n_ops = op_stack
        answer = max(answer,abs(n_nums[0]))
    return answer