#define _CRT_SECURE_NO_WARNINGS
// ���Ȱ��� �̽��� ����� ����� �ڵ� (ex : scanf ��� ��)

#include <stdio.h>

int main() {
    int a, b;

    printf("ù��° ������ �Է��ϼ���. >> ");
    scanf("%d", &a);
    // scanf_s : #define �ڵ� ���� ������� ���ȹ��� �ذ�
    // & : ������
    // scanf : ��Ÿ �ٸ� ������ input ���
    printf("�ι�° ������ �Է��ϼ���. >> ");
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

    printf("\nù��° �Ǽ��� �Է��ϼ���. >> ");
    scanf("%f", &a1);
    // scanf_s : #define �ڵ� ���� ������� ���ȹ��� �ذ�
    // & : ������
    // scanf : ��Ÿ �ٸ� ������ input ���
    printf("�ι�° �Ǽ��� �Է��ϼ���. >> ");
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

    printf("\nù��° �Ǽ��� �Է��ϼ���. >> ");
    scanf("%f", &a2);
    // scanf_s : #define �ڵ� ���� ������� ���ȹ��� �ذ�
    // & : ������
    // scanf : ��Ÿ �ٸ� ������ input ���
    printf("�ι�° �Ǽ��� �Է��ϼ���. >> ");
    scanf("%f", &b2);

    printf("%f + %f = %f\n", a2, b2, a2 + b2);
    printf("%f - %f = %f\n", a2, b2, a2 - b2);
    printf("%f * %f = %f\n", a2, b2, a2 * b2);
    printf("%f / %f = %f\n", a2, b2, a2 / b2);
}