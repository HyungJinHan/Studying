#include <stdio.h>

int main() {
	int a; // ���� ���� (integer)
	// ���� ���� : ���ĺ� ��ҹ���, _, ����(a2 O / 2a X)

	a = 10; // a�� 10�� ����
	printf("%d\n", a); // ��� : 10

	a = 100; // a�� 100�� ����
	printf("%d\n", a); // ��� : 100

	int b = 50; // ���� �ʱ�ȭ
	int c = 150;
	int sum = b + c;
	printf("%d + %d = %d\n", b, c, sum);
}