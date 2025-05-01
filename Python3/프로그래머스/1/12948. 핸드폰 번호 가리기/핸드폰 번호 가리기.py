def solution(phone_number):
    answer = ''
    exclude4 = len(phone_number) - 4 #뒤 4자리 제외한 길이
    for _ in range(exclude4):
        answer += "*"
    answer += phone_number[exclude4:]
    return answer