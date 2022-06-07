#include <stdio.h>

int main() {
    int a1 = 100;
    int b1 = 30;
    int add1 = a1 + b1;
    int subtract1 = a1 - b1;
    int multiply1 = a1 * b1;
    int devide1 = a1 / b1;
    int remainder1 = a1 % b1; // (나머지 연산자)
    // int : 32비트 (4바이트), 정수를 담는 변수
    printf("%d + %d = %d\n", a1, b1, add1); // 결과 : 100 + 30 = 130
    printf("%d - %d = %d\n", a1, b1, subtract1); // 결과 : 100 - 30 = 70
    printf("%d * %d = %d\n", a1, b1, multiply1); // 결과 : 100 * 30 = 3000
    printf("%d / %d = %d\n", a1, b1, devide1); // 결과 : 100 / 30 = 3 (정수로써 몫만을 표시)
    printf("%d %% %d = %d\n", a1, b1, remainder1); // 결과 : 100 % 30 = 10 (나눈 후의 나머지 값)

    float a2 = 9.3;
    float b2 = 3.14;
    float add2 = a2 + b2;
    float subtract2 = a2 - b2;
    float multiply2 = a2 * b2;
    float devide2 = a2 / b2;
    // float : 32비트 (4바이트), 실수를 담는 변수
    printf("%f + %f = %f\n", a2, b2, add2); // 결과 : 9.300000 + 3.140000 = 12.440001
    printf("%f - %f = %f\n", a2, b2, subtract2); // 결과 : 9.300000 - 3.140000 = 6.160000
    printf("%f * %f = %f\n", a2, b2, multiply2); // 결과 : 9.300000 * 3.140000 = 29.202002
    printf("%f / %f = %f\n", a2, b2, devide2); // 결과 : 9.300000 / 3.140000 = 2.961783

    double a3 = 9.3;
    double b3 = 3.14;
    double add3 = a3 + b3;
    double subtract3 = a3 - b3;
    double multiply3 = a3 * b3;
    double devide3 = a3 / b3;
    // double : 64비트 (8바이트), 실수를 담는 변수
    // → 저장용량이 큰 만큼 표현가능한 숫자도 커지며 오차가 줄어듬
    printf("%f + %f = %f\n", a3, b3, add3); // 결과 : 9.300000 + 3.140000 = 12.440000
    printf("%f - %f = %f\n", a3, b3, subtract3); // 결과 : 9.300000 - 3.140000 = 6.160000
    printf("%f * %f = %f\n", a3, b3, multiply3); // 결과 : 9.300000 * 3.140000 = 29.202000
    printf("%f / %f = %f\n", a3, b3, devide3); // 결과 : 9.300000 / 3.140000 = 2.961783
}
