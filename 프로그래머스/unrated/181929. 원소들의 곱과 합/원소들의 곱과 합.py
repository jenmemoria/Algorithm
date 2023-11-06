def solution(num_list):
    sum1 = 1
    sum2 = 0
    sum3 = 1
    for i in range(len(num_list)):
        sum1 *= num_list[i]
        print(sum1)
        sum2 += num_list[i]
        print(sum2)
    sum3 = sum2 * sum2
    if(sum1 < sum3):
        answer = 1
    else :
        answer = 0
    return answer