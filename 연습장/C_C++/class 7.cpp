#define _CRT_SECURE_NO_WARNINGS
// 보안관련 이슈를 띄우지 말라는 코드 (ex : scanf 사용 시)

#include <stdio.h>

int main() {
    int a, b;

    printf("첫번째 정수를 입력하세요. >> ");
    scanf("%d", &a);
    // scanf_s : #define 코드 외의 방법으로 보안문제 해결
    // & : 포인터
    // scanf : 기타 다른 언어에서의 input 기능
    printf("두번째 정수를 입력하세요. >> ");
    scanf("%d",&b);

    int add = a + b;
    int subtract = a - b;
    int multiply = a * b;
    int devide = a / b;
    int remainder = a % b;
    printf("%d + %d = %d\n", a, b, add);
    printf("%d - %d = %d\n", a, b, subtract);
    printf("%d * %d = %d\n", a, b, multiply);
    printf("%d / %d = %d\n", a, b, devide);
    printf("%d %% %d = %d\n", a, b, remainder);

    float a1, b1;

    printf("\n첫번째 실수를 입력하세요. >> ");
    scanf("%f", &a1);
    // scanf_s : #define 코드 외의 방법으로 보안문제 해결
    // & : 포인터
    // scanf : 기타 다른 언어에서의 input 기능
    printf("두번째 실수를 입력하세요. >> ");
    scanf("%f", &b1);

    float add1 = a1 + b1;
    float subtract1 = a1 - b1;
    float multiply1 = a1 * b1;
    float devide1 = a1 / b1;
    printf("%f + %f = %f\n", a1, b1, add1);
    printf("%f - %f = %f\n", a1, b1, subtract1);
    printf("%f * %f = %f\n", a1, b1, multiply1);
    printf("%f / %f = %f\n", a1, b1, devide1);

    float a2, b2;

    printf("\n첫번째 실수를 입력하세요. >> ");
    scanf("%f", &a2);
    // scanf_s : #define 코드 외의 방법으로 보안문제 해결
    // & : 포인터
    // scanf : 기타 다른 언어에서의 input 기능
    printf("두번째 실수를 입력하세요. >> ");
    scanf("%f", &b2);

    printf("%f + %f = %f\n", a2, b2, a2 + b2);
    printf("%f - %f = %f\n", a2, b2, a2 - b2);
    printf("%f * %f = %f\n", a2, b2, a2 * b2);
    printf("%f / %f = %f\n", a2, b2, a2 / b2);
}