def solution(polynomial):
    answer = ''
    x, num = 0, 0 # x는 x계수, num은 상수
    
    # "+"라는 구분자를 기준으로 각 항으로 나누어진 리스트로 변환.
    polynomial = polynomial.split(" + ")
    
    
    # 각 항을 반복
    for i in polynomial:
        
        # 항 'i'가 숫자로만 이루어져 있다면, 상수항으로 간주.
        if i.isnumeric():
            num += int(i)
            
        # 항 'i'가 숫자로 이루어져 있지 않다면, 'x'를 포함하는 항으로 간주.
        else :
            if len(i) == 1:
                x += 1 # 항의 길이가 1이면, 'x'의 계수가 1증가.
                        
        # 항의 길이가 1보다 크다면, 'x'다음에 계수가 있음. 마지막 문자 제외한 부분이 'x'의 계수.
            else:
                x += int(i[:-1])
                
     # x항이 0이 아니고
    if x != 0:
        # answer += (x == 1) and '' or str(x) # x의 계수가 1이면 x앞에 공백
        if x != 1:
            answer += str(x)
        answer += 'x'
        
    # '+'
    if answer != '' and num != 0:
        answer += ' + '
        
    # num가 0이 아닌 경우
    if num != 0 :
        answer += str(num)
        
    if x == 0 and num == 0 :
        answer = "0"
    
    
    print(answer)
    return answer
    