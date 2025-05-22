#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
 
// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    for(int i=0; i<numbers_len;i++)
    {
        for(int x=i+1; x<numbers_len; x++)
        {
            if(numbers[i]*numbers[x]>answer)
                answer=numbers[i]*numbers[x];
        }
    }
    return answer;
}