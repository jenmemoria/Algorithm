def solution(hp):
    cnt = 0
    
    cnt += hp // 5
    hp = hp % 5
    
    cnt += hp // 3
    hp = hp % 3
    
    cnt += hp // 1
    return cnt