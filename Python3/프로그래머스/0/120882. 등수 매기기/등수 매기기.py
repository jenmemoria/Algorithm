def solution(score):
    avg = [(x+y)/2 for x, y in score]
    
    _avg = avg[:]
    _avg.sort(reverse=True)
    
    answer = [_avg.index(x) + 1 for x in avg]
    return answer