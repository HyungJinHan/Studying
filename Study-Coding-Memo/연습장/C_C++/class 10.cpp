#include <stdio.h>

int main() {
	// ���������
	// +, -, *, /, =, %, +=, -=, *=, /=, %=, ++, --

	int a;
	a = 100;
	printf("a�� ���� %d�̾���.\n", a);

	a = a + 10;
	printf("a�� 10�� ���ؼ� %d�� �Ǿ���.\n", a);

	int b;
	b = 200;
	b += 20; // b = b + 20
	printf("\nb�� 20�� ���ؼ� %d�� �Ǿ���.\n", b);

	b *= 10; // b = b * 10
	printf("b�� 10�� ���ؼ� %d�� �Ǿ���.\n", b);

	b -= 1000; // b = b - 1000
	printf("b�� 1000�� ���� %d�� �Ǿ���.\n", b);

	b %= 7; // b = b % 7
	printf("b�� 7�� ���� �������� %d�̴�.\n", b);

	int c;
	c = 50;
	printf("\nc�� %d�̴�.\n", c);
	c++; // c = c + 1, c += 1
	printf("c++�� ����� %d�̴�.\n", c);

	int d;
	d = 30;
	printf("\nd�� %d�̴�.\n", d);
	d--; // d = d - 1, d -= 1
	printf("d--�� ����� %d�̴�.\n", d);
}