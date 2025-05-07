def solution(s) :
    answer = ''
    index = 0
    
    for word in s:
        #공백이면
        if word.isspace() :
            index = 0 #인덱스 초기화
            answer += ' '
            continue
        
        #문자가 존재한다면
        else :
            if index % 2 == 0:
                answer += word.upper()
            else :
                answer += word.lower()
        index += 1 #인덱스 ++1 
    return answer