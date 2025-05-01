def solution(num):
    count = 0
    while count <= 500:
        if num == 1 :
            return count
        elif num % 2 == 0:
            num = num / 2
        elif num % 2 != 0:
            num = num * 3 + 1
        count += 1 # 1-1, 1-2 한 번 다 했으니까
    return -1
    
        
    return count