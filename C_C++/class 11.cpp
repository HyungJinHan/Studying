#include <stdio.h>

int main() {
	int a, b;

	printf("a�� �Է��ϼ���. >> ");
	scanf_s("%d", &a);

	getchar(); // scanf�� ���õǴ� ������ ���� �Է¹��� ���� �ڵ�

	printf("b�� �Է��ϼ���. >> ");
	scanf_s("%d", &b);

	// Comparison Operator (�� ������) - Boolean : ��, ����
	bool p = a > b;
	bool p1 = a >= b;
	bool q = a < b;
	bool q1 = a <= b;
	bool r = a == b; // ����
	bool r1 = a != b; // �ٸ���
	printf("%d\n", p);
	// ��� : 0 false (a=5, b=10) / 0 false (a=5, b=5)
	printf("%d\n", p1);
	// ��� : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", q);
	// ��� : 1 true (a=5, b=10) / 0 false (a=5, b=5)
	printf("%d\n", q1);
	// ��� : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", r);
	// ��� : 0 false (a=5, b=10) / 1 true (a=5, b=5)
	printf("%d\n", r1);
	// ��� : 1 true (a=5, b=10) / 0 false (a=5, b=5)

	// Logical Operator (�� ������)
	bool l = a >= 1 && a <= 10; // �׸���
	bool l1 = a >= 1 || a <= 10; // �Ǵ�
	bool l2 = !l1; // �ݴ� (true�� false, false�� true)
	printf("\n%d\n", l); // 0 false (a = 20)
	printf("%d\n", l1); // 1 true (a = 20)
	printf("%d\n", l2); // 0 false (l1 = true)
}