#include <stdio.h>

int main() {
	int a1 = 100;
	int b1 = 30;
	int add1 = a1 + b1;
	int subtract1 = a1 - b1;
	int multiply1 = a1 * b1;
	int devide1 = a1 / b1;
	int remainder1 = a1 % b1; // (������ ������)
	// int : 32��Ʈ (4����Ʈ), ������ ��� ����
	printf("%d + %d = %d\n", a1, b1 ,add1); // ��� : 100 + 30 = 130
	printf("%d - %d = %d\n", a1, b1, subtract1); // ��� : 100 - 30 = 70
	printf("%d * %d = %d\n", a1, b1, multiply1); // ��� : 100 * 30 = 3000
	printf("%d / %d = %d\n", a1, b1, devide1); // ��� : 100 / 30 = 3 (�����ν� ���� ǥ��)
	printf("%d %% %d = %d\n", a1, b1, remainder1); // ��� : 100 % 30 = 10 (���� ���� ������ ��)
	
	float a2 = 9.3;
	float b2 = 3.14;
	float add2 = a2 + b2;
	float subtract2 = a2 - b2;
	float multiply2 = a2 * b2;
	float devide2 = a2 / b2;
	// float : 32��Ʈ (4����Ʈ), �Ǽ��� ��� ����
	printf("%f + %f = %f\n", a2, b2, add2); // ��� : 9.300000 + 3.140000 = 12.440001
	printf("%f - %f = %f\n", a2, b2, subtract2); // ��� : 9.300000 - 3.140000 = 6.160000
	printf("%f * %f = %f\n", a2, b2, multiply2); // ��� : 9.300000 * 3.140000 = 29.202002
	printf("%f / %f = %f\n", a2, b2, devide2); // ��� : 9.300000 / 3.140000 = 2.961783
	
	double a3 = 9.3;
	double b3 = 3.14;
	double add3 = a3 + b3;
	double subtract3 = a3 - b3;
	double multiply3 = a3 * b3;
	double devide3 = a3 / b3;
	// double : 64��Ʈ (8����Ʈ), �Ǽ��� ��� ����
	// �� ����뷮�� ū ��ŭ ǥ�������� ���ڵ� Ŀ���� ������ �پ��
	printf("%f + %f = %f\n", a3, b3, add3); // ��� : 9.300000 + 3.140000 = 12.440000
	printf("%f - %f = %f\n", a3, b3, subtract3); // ��� : 9.300000 - 3.140000 = 6.160000
	printf("%f * %f = %f\n", a3, b3, multiply3); // ��� : 9.300000 * 3.140000 = 29.202000
	printf("%f / %f = %f\n", a3, b3, devide3); // ��� : 9.300000 / 3.140000 = 2.961783
}