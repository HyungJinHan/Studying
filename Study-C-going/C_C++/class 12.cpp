#include <stdio.h>

int main() {
	int n;
	printf("���ڸ� �Է��ϼ���. >> ");
	scanf_s("%d", &n);

	// n�� ¦���� �� n % 2 == 0�̹Ƿ� true ������ ���
	// n�� Ȧ���� �� n % 2 != 0�̹Ƿ� false ������ ���
	if (n % 2 == 0) {
		printf("\n�Է��� n(%d)�� ¦���Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� Ȧ���Դϴ�.\n", n);
	}

	// n�� ¦���� �� n % 2�� ���� 0�̹Ƿ� false ������ ���
	// n�� Ȧ���� �� n % 2�� ���� 1�̹Ƿ� true ������ ���
	if (n % 2) {
		printf("\n�Է��� n(%d)�� Ȧ���Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� ¦���Դϴ�.\n", n);
	}

	// else if��
	// n > 0�̸� ����̹Ƿ� true ������ ���
	// n == 0�̸� 0�̹Ƿ� else if�� true ������ ���
	// n < 0�̸� �����̹Ƿ� else if�� false ������ ���
	if (n > 0) {
		printf("\n�Է��� n(%d)�� ����Դϴ�.\n", n);
	}
	else if (n == 0) {
		printf("\n�Է��� n(%d)�� 0�Դϴ�.\n", n);
	}
	else {
		printf("\n�Է��� n(%d)�� �����Դϴ�.\n", n);
	}

	int a, b, c;
	printf("\n���� a�� �Է��ϼ���. >> ");
	scanf_s("%d", &a);
	printf("\n���� b�� �Է��ϼ���. >> ");
	scanf_s("%d", &b);
	printf("\n���� c�� �Է��ϼ���. >> ");
	scanf_s("%d", &c);

	// if ��ø �� �߰�ȣ ����
	if (a > b) {
		if (a > c)
			printf("\na(%d)�� ���� Ů�ϴ�.\n", a); // a > c
		else
			printf("\nc(%d)�� ���� Ů�ϴ�.\n", c); // c > a
	}
	else if (b > c)
		printf("\nb(%d)�� ���� Ů�ϴ�.\n", b); // b > c
	else
		printf("\nc(%d)�� ���� Ů�ϴ�.\n", c); // c > b
}