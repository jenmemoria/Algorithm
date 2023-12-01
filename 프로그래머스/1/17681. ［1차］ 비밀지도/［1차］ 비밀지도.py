def solution(n, arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2) :
        # 10진수를 2진수로 바꾸기
        value = bin(x | y)[2:]
        
        # 이진수 문자열의 길이가 n보다 작으면 앞에 "0"을 채워줌
        if len(value) < n :
            value = "0"*(n - len(value)) + value
            
        # 2진수 중, 1이면 "#"으로 바꾸고 0이면 " "(공백)으로 바꾸기
        value = value.replace("0", " ").replace("1", "#")
    
        answer.append(value)
    
    return answer