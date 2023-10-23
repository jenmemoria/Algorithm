def solution(a, b):
    
    n1 = int(str(a) + str(b))
    n2 = int(str(b) + str(a))
    
    return n1 if n1 >= n2 else n2    