from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = []
    bunmo = 0
    bunja = 0
    
    #통분하기
    bunmo = denom1 * denom2 # 약분하기 전 분모
    bunja = numer1 * denom2 + numer2 * denom1 # 약분하기 전 분자
    
    
    # 기약분수 만들기
    for x in range(bunmo, 1, -1):
        if(bunja % x == 0 and bunmo % x == 0) :
            bunja /= x
            bunmo /= x     
        
    # 빈 리스트에 하나씩 추가하기 (앞에서부터 추가)
    answer = [bunja, bunmo]
    return answer