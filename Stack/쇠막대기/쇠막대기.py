def solution(arrangement):
    stack = []
    answer = 0
    for s in arrangement:
        if s == '(':
            stack.append(s)
            last = s
        else:
            stack.pop()
            if  last == '(':
                answer += len(stack)
            else:
                answer +=1
            last = s
    return answer