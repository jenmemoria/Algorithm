def solution(name, yearning, photo):
    answer = []
    
    for i in photo :
        score = 0
        for k in i:
            if k in name:
                score += yearning[name.index(k)]    
            
        answer.append(score)
        
    return answer