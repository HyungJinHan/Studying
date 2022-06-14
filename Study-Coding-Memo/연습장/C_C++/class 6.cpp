#include <stdio.h>

int main() {
	printf("%d %d %d %d\n", sizeof(int), sizeof(char), sizeof(float), sizeof(double));

	int a; char b; float c; double d;

	printf("%d %d %d %d\n", sizeof(a), sizeof(b), sizeof(c), sizeof(d));

	// ��� : 4(int - 4����Ʈ) 1(char - 1����Ʈ) 4(float - 4����Ʈ) 8(double - 4����Ʈ)
	// sizeof(x) : x�� ũ�⸦ �˷���
	// x : int, float ����� ������Ÿ��, ������ �̸��� ��

	int a1 = 3.14;
	double b1 = 10;
	printf("%d, %f\n", a1, b1);
	// ��� : 3, 10.000000
	// �Ǽ��� ������ ������ ���� �� ����
	// ������ �Ǽ��� ������ ���� �� ����

	int math = 90, korean = 95, english = 96;
	int sum = math + korean + english; // int������ ����
	double avg = sum / 3;
	printf("%f\n", avg);
	// ���� : 93.666667 / ��� : 93.000000
	
	// �� ���� ������� �Ǽ��� �����1 ��

	int math1 = 90, korean1 = 95, english1 = 96;
	double sum1 = math1 + korean1 + english1; // double������ ����
	double avg1 = sum1 / 3;
	printf("%f\n", avg1);
	// ���� : 93.666667 / ��� : 93.666667
	
	// �� ���� ������� �Ǽ��� �����2 ��

	int math2 = 90, korean2 = 95, english2 = 96;
	int sum2 = math2 + korean2 + english2;
	double avg2 = (double)sum2 / 3; // �ӽ÷� double������ ����
	printf("%f\n", avg2);
	// ���� : 93.666667 / ��� : 93.666667

	double a2 = 50.5;
	int b2 = 10;
	double a2b2 = a2 / b2;
	printf("%f\n", a2b2);
	// ��� : 5.050000
	// �Ǽ� / ���� = �Ǽ�

	double a3 = 100.5;
	double b3 = 20.5;
	double a3b3 = a3 / b3;
	printf("%f\n", a3b3);
	// ��� : 4.902439
	// �Ǽ� / �Ǽ� = �Ǽ�

	int a4 = 100.5;
	int b4 = 50;
	double a4b4 = a4 / b4;
	printf("%f\n", a4b4);
	// ��� : 2.000000
	// ���� / ���� = ����

	// �� �� (-, * ����)
	// ���� + ���� = ����
	// ���� + �Ǽ� = �Ǽ� (�Ǽ��� ������ ũ�Ⱑ �� ũ�⶧����)
	// �Ǽ� + �Ǽ� = �Ǽ�
}
