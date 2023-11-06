def solution(a, b, c):
    answer = a + b + c
    sum2 = a**2 + b**2 + c**2
    sum3 = a**3 + b**3 + c**3
    if (a == b and b == c) :
        answer = answer * sum2 * sum3
    elif (a == b or a == c or b == c) :
        answer = answer * sum2
    return answer