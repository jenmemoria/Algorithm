def solution(n, control):
    
    answer = {"w" : 1, "s" : -1, "d" : 10, "a" : -10 }
    for i in control :
        n += answer[i]
    return n