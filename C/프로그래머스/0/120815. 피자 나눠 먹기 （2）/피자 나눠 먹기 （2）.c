#include <stdio.h>

// 최대공약수 함수
int gcd(int a, int b) {
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int solution(int n) {
    int g = gcd(6, n);          // 6과 n의 최대공약수
    return n / g;               // 최소 공배수를 6으로 나눈 값이 최소 판 수
}