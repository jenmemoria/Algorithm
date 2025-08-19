def solution(lines):
    answer = 0
    line = [0 for _ in range(200)]
    for i in range(3):
        start = lines[i][0]
        end = lines[i][1]
        for j in range(start,end):
            line[j+100]+=1
    for i in line:
        if i>=2: 
            answer+=1
    return answer